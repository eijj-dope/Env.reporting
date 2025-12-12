import os
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from models import db, Category, Status, Report

# Load env variables
load_dotenv()

app = Flask(__name__, template_folder='templates', static_folder='static')
# Set the secret key
app.secret_key = 'group-3'

# File upload configuration
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit file size to 16MB

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# PostgreSQL connection
DB_URL = os.getenv("DATABASE_URL")
if os.getenv("USE_SSL", "false").lower() == "true" and DB_URL and "sslmode" not in DB_URL:
    DB_URL += "?sslmode=require"

app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db.init_app(app)
migrate = Migrate(app, db)

# -----------------------------
# Routes
# -----------------------------
@app.route("/")
def index():
    recent = Report.query.order_by(Report.created_at.desc()).limit(5).all()
    return render_template("index.html", recent=recent, title="Home")

@app.route("/submit", methods=["POST"])
def submit_report():
    title = request.form.get("title")
    description = request.form.get("description")
    category_name = request.form.get("category")
    address = request.form.get("address")
    photo = request.files.get("photo")

    # Validation
    if not title or not category_name or not address:
        flash("Title, category, and address are required.", "danger")
        return redirect(url_for("index"))

    # Handle photo upload
    photo_url = ""
    if photo and photo.filename != "":
        filename = secure_filename(photo.filename)
        photo_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        photo.save(photo_path)
        photo_url = url_for('uploaded_file', filename=filename)

    # Get category ID
    category = Category.query.filter_by(category_name=category_name).first()
    if not category:
        flash("Invalid category selected.", "danger")
        return redirect(url_for("index"))

    # Get default status ("Pending")
    status = Status.query.filter_by(status_name="Pending").first()

    # Create new report
    new_report = Report(
        title=title,
        description=description,
        category_id=category.category_id,
        status_id=status.status_id,
        address=address,
        photo_url=photo_url
    )

    db.session.add(new_report)
    db.session.commit()
    flash("Report submitted. Thank you!", "success")
    return redirect(url_for("index"))

@app.route("/reports")
def reports():
    category_filter = request.args.get("category")  # Get category filter from query string

    # Base query
    query = db.session.query(
        Report,
        Category.category_name.label("category_name"),
        Status.status_name.label("status_name")
    ).join(Category, Report.category_id == Category.category_id
    ).join(Status, Report.status_id == Status.status_id)

    # Apply category filter if provided
    if category_filter:
        query = query.filter(Category.category_name == category_filter)

    all_reports = query.order_by(Report.created_at.desc()).all()

    # Get all categories for dropdown/filter options
    categories = Category.query.all()

    return render_template(
        "report_list.html",
        reports=all_reports,
        categories=categories,
        selected_category=category_filter
    )

@app.route("/api/reports")
def api_reports():
    reports = Report.query.order_by(Report.created_at.desc()).all()
    return jsonify([r.to_dict() for r in reports])

# -----------------------------
# Admin Routes
# -----------------------------
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "Admin@123")

@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        password = request.form.get("password")
        if password == ADMIN_PASSWORD:
            session['admin_logged_in'] = True
            flash("Welcome, Admin!", "success")
            return redirect(url_for("admin"))
        else:
            flash("Incorrect password.", "danger")
            return redirect(url_for("admin_login"))
    return render_template("admin_login.html")

@app.route("/admin")
def admin():
    if not session.get("admin_logged_in"):
        flash("Please log in as admin first.", "danger")
        return redirect(url_for("admin_login"))

    all_reports = db.session.query(
        Report,
        Category.category_name.label("category_name"),
        Status.status_name.label("status_name")
    ).join(Category, Report.category_id == Category.category_id
    ).join(Status, Report.status_id == Status.status_id
    ).order_by(Report.created_at.desc()).all()

    return render_template("admin.html", reports=all_reports)

@app.route("/admin/logout")
def admin_logout():
    session.pop("admin_logged_in", None)
    flash("Logged out successfully.", "success")
    return redirect(url_for("index"))

@app.route("/admin/update/<int:report_id>", methods=["POST"])
def admin_update(report_id):
    report = Report.query.get_or_404(report_id)
    new_status_name = request.form.get("status")

    if new_status_name:
        new_status = Status.query.filter_by(status_name=new_status_name).first()
        if new_status:
            report.status_id = new_status.status_id
            db.session.commit()
            flash("Status updated.", "success")
        else:
            flash("Invalid status.", "danger")
    else:
        flash("No status provided.", "danger")
    return redirect(url_for("admin"))

@app.route("/report")
def report_form():
    categories = Category.query.all()
    return render_template("report_form.html", categories=categories)

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route("/admin/delete/<int:report_id>", methods=["POST"])
def admin_delete(report_id):
    if not session.get("admin_logged_in"):
        flash("Please log in as admin first.", "danger")
        return redirect(url_for("admin_login"))

    report = Report.query.get_or_404(report_id)

    if report.photo_url:
        filename = os.path.basename(report.photo_url)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if os.path.exists(file_path):
            os.remove(file_path)

    db.session.delete(report)
    db.session.commit()
    flash(f"Report ID {report_id} deleted successfully.", "success")
    return redirect(url_for("admin"))

# -----------------------------
# Run the app
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
