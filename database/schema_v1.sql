-- Schema Version: v1
-- Description: Initial database structure for ENV Reporting System

-- Table: alembic_version
CREATE TABLE public.alembic_version (
    version_num VARCHAR(32) NOT NULL
);

ALTER TABLE public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);

-- Table: categories
CREATE TABLE public.categories (
    id INTEGER NOT NULL,
    name VARCHAR(100) NOT NULL
);

CREATE SEQUENCE public.categories_id_seq
    START WITH 1
    INCREMENT BY 1;

ALTER TABLE public.categories 
    ALTER COLUMN id SET DEFAULT nextval('public.categories_id_seq');

ALTER TABLE public.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (id);

ALTER TABLE public.categories
    ADD CONSTRAINT categories_name_key UNIQUE (name);

-- Table: statuses
CREATE TABLE public.statuses (
    id INTEGER NOT NULL,
    name VARCHAR(50) NOT NULL
);

CREATE SEQUENCE public.statuses_id_seq
    START WITH 1
    INCREMENT BY 1;

ALTER TABLE public.statuses
    ALTER COLUMN id SET DEFAULT nextval('public.statuses_id_seq');

ALTER TABLE public.statuses
    ADD CONSTRAINT statuses_pkey PRIMARY KEY (id);

ALTER TABLE public.statuses
    ADD CONSTRAINT statuses_name_key UNIQUE (name);

-- Table: reports
CREATE TABLE public.reports (
    id INTEGER NOT NULL,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    address VARCHAR(300) NOT NULL,
    photo_url VARCHAR(500),
    created_at TIMESTAMP WITHOUT TIME ZONE,
    updated_at TIMESTAMP WITHOUT TIME ZONE,
    category_id INTEGER,
    status_id INTEGER
);

CREATE SEQUENCE public.reports_id_seq
    START WITH 1
    INCREMENT BY 1;

ALTER TABLE public.reports
    ALTER COLUMN id SET DEFAULT nextval('public.reports_id_seq');

ALTER TABLE public.reports
    ADD CONSTRAINT reports_pkey PRIMARY KEY (id);

ALTER TABLE public.reports
    ADD CONSTRAINT reports_category_id_fkey FOREIGN KEY (category_id) REFERENCES public.categories(id);

ALTER TABLE public.reports
    ADD CONSTRAINT reports_status_id_fkey FOREIGN KEY (status_id) REFERENCES public.statuses(id);

ALTER TABLE public.reports DROP COLUMN id;

ALTER TABLE public.reports
ADD COLUMN id SERIAL PRIMARY KEY;
