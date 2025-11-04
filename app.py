import os
from werkzeug.utils import secure_filename
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import session
from flask import send_from_directory
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask import Flask, render_template

# Load env variables
load_dotenv()

app = Flask(__name__, template_folder='templates', static_folder='static')

# Set the secret key
app.secret_key = 'group-3'

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit file size to 16MB

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# PostgreSQL connection
DB_URL = os.getenv("DATABASE_URL")
if DB_URL and "sslmode" not in DB_URL:
    DB_URL += "?sslmode=require"

app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# -----------------------------
# Database Model
# -----------------------------
class Report(db.Model):
    __tablename__ = "reports"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    category = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(300), nullable=False)  # replaced latitude/longitude
    photo_url = db.Column(db.String(500), nullable=True)
    status = db.Column(db.String(50), default="Pending")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "address": self.address,
            "photo_url": self.photo_url,
            "status": self.status,
            "created_at": self.created_at.isoformat()
        }

# -----------------------------
# Routes
# -----------------------------
@app.route("/")
def index():
    recent = Report.query.order_by(Report.created_at.desc()).limit(5).all()
    return render_template("index.html", recent=recent)

@app.route("/submit", methods=["POST"])
def submit_report():
    title = request.form.get("title")
    description = request.form.get("description")
    category = request.form.get("category")
    address = request.form.get("address")
    photo = request.files.get("photo")

    # Validation
    if not title or not category or not address:
        flash("Title, category, and address are required.", "danger")
        return redirect(url_for("index"))

    # Handle photo upload
    photo_url = ""
    if photo and photo.filename != "":
        filename = secure_filename(photo.filename)
        photo_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        photo.save(photo_path)
        photo_url = f"/uploads/{filename}"

    new = Report(
        title=title,
        description=description,
        category=category,
        address=address,
        photo_url=photo_url,
        status="Pending"
    )
    db.session.add(new)
    db.session.commit()
    flash("Report submitted. Thank you!", "success")
    return redirect(url_for("index"))

@app.route("/reports")
def reports():
    all_reports = Report.query.order_by(Report.created_at.desc()).all()
    return render_template("report_list.html", reports=all_reports)

@app.route("/api/reports")
def api_reports():
    reports = Report.query.order_by(Report.created_at.desc()).all()
    return jsonify([r.to_dict() for r in reports])

ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin123")

@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        password = request.form.get("password")
        if password == ADMIN_PASSWORD:
            session['admin_logged_in'] = True
            flash("Welcome, Admin!", "success")  # This flash will appear in admin page
            return redirect(url_for("admin"))  # redirect to admin dashboard
        else:
            flash("Incorrect password.", "danger")
            return redirect(url_for("admin_login"))
    return render_template("admin_login.html")


@app.route("/admin")
def admin():
    if not session.get("admin_logged_in"):
        flash("Please log in as admin first.", "danger")
        return redirect(url_for("admin_login"))
    
    all_reports = Report.query.order_by(Report.created_at.desc()).all()
    return render_template("admin.html", reports=all_reports)

@app.route("/admin/logout")
def admin_logout():
    session.pop("admin_logged_in", None)
    flash("Logged out successfully.", "success")
    return redirect(url_for("index"))

@app.route("/admin/update/<int:report_id>", methods=["POST"])
def admin_update(report_id):
    report = Report.query.get_or_404(report_id)
    new_status = request.form.get("status")
    if new_status:
        report.status = new_status
        db.session.commit()
        flash("Status updated.", "success")
    return redirect(url_for("admin"))

@app.route("/report")
def report_form():
    return render_template("report_form.html")

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Remove map routes — no longer used
# /map and /sample-data removed

if __name__ == "__main__":
    app.run(debug=True)
