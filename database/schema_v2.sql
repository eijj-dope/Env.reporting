-- Schema for Reporting System v2

-- Table: alembic_version
CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL,
    PRIMARY KEY(version_num)
);

-- Table: categories
CREATE TABLE public.categories (
    category_id SERIAL PRIMARY KEY,
    category_name character varying(100) NOT NULL UNIQUE
);

-- Table: statuses
CREATE TABLE public.statuses (
    status_id SERIAL PRIMARY KEY,
    status_name character varying(50) NOT NULL UNIQUE
);

-- Table: reports
CREATE TABLE public.reports (
    id SERIAL PRIMARY KEY,
    title character varying(200) NOT NULL,
    description text,
    address character varying(300) NOT NULL,
    photo_url character varying(500),
    created_at timestamp without time zone DEFAULT now(),
    updated_at timestamp without time zone DEFAULT now(),
    category_id integer REFERENCES public.categories(category_id),
    status_id integer REFERENCES public.statuses(status_id)
);
