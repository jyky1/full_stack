--
-- PostgreSQL database dump
--

-- Dumped from database version 12.12 (Ubuntu 12.12-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.12 (Ubuntu 12.12-0ubuntu0.20.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: author; Type: TABLE; Schema: public; Owner: zhyldyzbek
--

CREATE TABLE public.author (
    id integer NOT NULL,
    name character varying(20),
    age integer
);


ALTER TABLE public.author OWNER TO zhyldyzbek;

--
-- Name: author_id_seq; Type: SEQUENCE; Schema: public; Owner: zhyldyzbek
--

CREATE SEQUENCE public.author_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.author_id_seq OWNER TO zhyldyzbek;

--
-- Name: author_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: zhyldyzbek
--

ALTER SEQUENCE public.author_id_seq OWNED BY public.author.id;


--
-- Name: autobiografia; Type: TABLE; Schema: public; Owner: zhyldyzbek
--

CREATE TABLE public.autobiografia (
    id integer NOT NULL,
    body text,
    create_at date,
    author_id integer
);


ALTER TABLE public.autobiografia OWNER TO zhyldyzbek;

--
-- Name: autobiografia_id_seq; Type: SEQUENCE; Schema: public; Owner: zhyldyzbek
--

CREATE SEQUENCE public.autobiografia_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.autobiografia_id_seq OWNER TO zhyldyzbek;

--
-- Name: autobiografia_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: zhyldyzbek
--

ALTER SEQUENCE public.autobiografia_id_seq OWNED BY public.autobiografia.id;


--
-- Name: blogger; Type: TABLE; Schema: public; Owner: zhyldyzbek
--

CREATE TABLE public.blogger (
    id integer NOT NULL,
    name character varying(20)
);


ALTER TABLE public.blogger OWNER TO zhyldyzbek;

--
-- Name: blogger_id_seq; Type: SEQUENCE; Schema: public; Owner: zhyldyzbek
--

CREATE SEQUENCE public.blogger_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.blogger_id_seq OWNER TO zhyldyzbek;

--
-- Name: blogger_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: zhyldyzbek
--

ALTER SEQUENCE public.blogger_id_seq OWNED BY public.blogger.id;


--
-- Name: dev_proj; Type: TABLE; Schema: public; Owner: zhyldyzbek
--

CREATE TABLE public.dev_proj (
    dev_id integer,
    proj_id integer
);


ALTER TABLE public.dev_proj OWNER TO zhyldyzbek;

--
-- Name: developer; Type: TABLE; Schema: public; Owner: zhyldyzbek
--

CREATE TABLE public.developer (
    id integer NOT NULL,
    name character varying(20),
    count_project integer
);


ALTER TABLE public.developer OWNER TO zhyldyzbek;

--
-- Name: developer_id_seq; Type: SEQUENCE; Schema: public; Owner: zhyldyzbek
--

CREATE SEQUENCE public.developer_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.developer_id_seq OWNER TO zhyldyzbek;

--
-- Name: developer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: zhyldyzbek
--

ALTER SEQUENCE public.developer_id_seq OWNED BY public.developer.id;


--
-- Name: post; Type: TABLE; Schema: public; Owner: zhyldyzbek
--

CREATE TABLE public.post (
    id integer NOT NULL,
    doby text,
    created_at date,
    blogger_id integer
);


ALTER TABLE public.post OWNER TO zhyldyzbek;

--
-- Name: post_id_seq; Type: SEQUENCE; Schema: public; Owner: zhyldyzbek
--

CREATE SEQUENCE public.post_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.post_id_seq OWNER TO zhyldyzbek;

--
-- Name: post_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: zhyldyzbek
--

ALTER SEQUENCE public.post_id_seq OWNED BY public.post.id;


--
-- Name: product; Type: TABLE; Schema: public; Owner: zhyldyzbek
--

CREATE TABLE public.product (
    id integer NOT NULL,
    name character varying(20) NOT NULL,
    price integer,
    CONSTRAINT product_price_check CHECK ((price > 0))
);


ALTER TABLE public.product OWNER TO zhyldyzbek;

--
-- Name: product2; Type: TABLE; Schema: public; Owner: zhyldyzbek
--

CREATE TABLE public.product2 (
    id integer NOT NULL,
    name character varying(20)
);


ALTER TABLE public.product2 OWNER TO zhyldyzbek;

--
-- Name: product2_id_seq; Type: SEQUENCE; Schema: public; Owner: zhyldyzbek
--

CREATE SEQUENCE public.product2_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.product2_id_seq OWNER TO zhyldyzbek;

--
-- Name: product2_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: zhyldyzbek
--

ALTER SEQUENCE public.product2_id_seq OWNED BY public.product2.id;


--
-- Name: product_id_seq; Type: SEQUENCE; Schema: public; Owner: zhyldyzbek
--

CREATE SEQUENCE public.product_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.product_id_seq OWNER TO zhyldyzbek;

--
-- Name: product_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: zhyldyzbek
--

ALTER SEQUENCE public.product_id_seq OWNED BY public.product.id;


--
-- Name: project; Type: TABLE; Schema: public; Owner: zhyldyzbek
--

CREATE TABLE public.project (
    id integer NOT NULL,
    title character varying(50),
    tz text,
    start date
);


ALTER TABLE public.project OWNER TO zhyldyzbek;

--
-- Name: project_id_seq; Type: SEQUENCE; Schema: public; Owner: zhyldyzbek
--

CREATE SEQUENCE public.project_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.project_id_seq OWNER TO zhyldyzbek;

--
-- Name: project_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: zhyldyzbek
--

ALTER SEQUENCE public.project_id_seq OWNED BY public.project.id;


--
-- Name: author id; Type: DEFAULT; Schema: public; Owner: zhyldyzbek
--

ALTER TABLE ONLY public.author ALTER COLUMN id SET DEFAULT nextval('public.author_id_seq'::regclass);


--
-- Name: autobiografia id; Type: DEFAULT; Schema: public; Owner: zhyldyzbek
--

ALTER TABLE ONLY public.autobiografia ALTER COLUMN id SET DEFAULT nextval('public.autobiografia_id_seq'::regclass);


--
-- Name: blogger id; Type: DEFAULT; Schema: public; Owner: zhyldyzbek
--

ALTER TABLE ONLY public.blogger ALTER COLUMN id SET DEFAULT nextval('public.blogger_id_seq'::regclass);


--
-- Name: developer id; Type: DEFAULT; Schema: public; Owner: zhyldyzbek
--

ALTER TABLE ONLY public.developer ALTER COLUMN id SET DEFAULT nextval('public.developer_id_seq'::regclass);


--
-- Name: post id; Type: DEFAULT; Schema: public; Owner: zhyldyzbek
--

ALTER TABLE ONLY public.post ALTER COLUMN id SET DEFAULT nextval('public.post_id_seq'::regclass);


--
-- Name: product id; Type: DEFAULT; Schema: public; Owner: zhyldyzbek
--

ALTER TABLE ONLY public.product ALTER COLUMN id SET DEFAULT nextval('public.product_id_seq'::regclass);


--
-- Name: product2 id; Type: DEFAULT; Schema: public; Owner: zhyldyzbek
--

ALTER TABLE ONLY public.product2 ALTER COLUMN id SET DEFAULT nextval('public.product2_id_seq'::regclass);


--
-- Name: project id; Type: DEFAULT; Schema: public; Owner: zhyldyzbek
--

ALTER TABLE ONLY public.project ALTER COLUMN id SET DEFAULT nextval('public.project_id_seq'::regclass);


--
-- Data for Name: author; Type: TABLE DATA; Schema: public; Owner: zhyldyzbek
--

COPY public.author (id, name, age) FROM stdin;
\.


--
-- Data for Name: autobiografia; Type: TABLE DATA; Schema: public; Owner: zhyldyzbek
--

COPY public.autobiografia (id, body, create_at, author_id) FROM stdin;
\.


--
-- Data for Name: blogger; Type: TABLE DATA; Schema: public; Owner: zhyldyzbek
--

COPY public.blogger (id, name) FROM stdin;
1	blogger1
2	blogger2
3	blogger3
4	blogger4
\.


--
-- Data for Name: dev_proj; Type: TABLE DATA; Schema: public; Owner: zhyldyzbek
--

COPY public.dev_proj (dev_id, proj_id) FROM stdin;
\.


--
-- Data for Name: developer; Type: TABLE DATA; Schema: public; Owner: zhyldyzbek
--

COPY public.developer (id, name, count_project) FROM stdin;
\.


--
-- Data for Name: post; Type: TABLE DATA; Schema: public; Owner: zhyldyzbek
--

COPY public.post (id, doby, created_at, blogger_id) FROM stdin;
1	first post	2010-10-10	1
2	second post	2011-11-11	1
3	good bye	2012-12-12	1
4	first post	2003-01-21	2
5	first post	2010-10-10	3
6	second post	2011-11-11	3
7	no author	2013-10-10	\N
\.


--
-- Data for Name: product; Type: TABLE DATA; Schema: public; Owner: zhyldyzbek
--

COPY public.product (id, name, price) FROM stdin;
2	iphone10	10000
3	iphone11	11000
4	iphone12	12000
5	iphone13	13000
6	iphone13	11500
\.


--
-- Data for Name: product2; Type: TABLE DATA; Schema: public; Owner: zhyldyzbek
--

COPY public.product2 (id, name) FROM stdin;
1	zhanbolot
2	jonson
\.


--
-- Data for Name: project; Type: TABLE DATA; Schema: public; Owner: zhyldyzbek
--

COPY public.project (id, title, tz, start) FROM stdin;
\.


--
-- Name: author_id_seq; Type: SEQUENCE SET; Schema: public; Owner: zhyldyzbek
--

SELECT pg_catalog.setval('public.author_id_seq', 1, false);


--
-- Name: autobiografia_id_seq; Type: SEQUENCE SET; Schema: public; Owner: zhyldyzbek
--

SELECT pg_catalog.setval('public.autobiografia_id_seq', 1, false);


--
-- Name: blogger_id_seq; Type: SEQUENCE SET; Schema: public; Owner: zhyldyzbek
--

SELECT pg_catalog.setval('public.blogger_id_seq', 4, true);


--
-- Name: developer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: zhyldyzbek
--

SELECT pg_catalog.setval('public.developer_id_seq', 1, false);


--
-- Name: post_id_seq; Type: SEQUENCE SET; Schema: public; Owner: zhyldyzbek
--

SELECT pg_catalog.setval('public.post_id_seq', 7, true);


--
-- Name: product2_id_seq; Type: SEQUENCE SET; Schema: public; Owner: zhyldyzbek
--

SELECT pg_catalog.setval('public.product2_id_seq', 1, false);


--
-- Name: product_id_seq; Type: SEQUENCE SET; Schema: public; Owner: zhyldyzbek
--

SELECT pg_catalog.setval('public.product_id_seq', 6, true);


--
-- Name: project_id_seq; Type: SEQUENCE SET; Schema: public; Owner: zhyldyzbek
--

SELECT pg_catalog.setval('public.project_id_seq', 1, false);


--
-- Name: author author_pkey; Type: CONSTRAINT; Schema: public; Owner: zhyldyzbek
--

ALTER TABLE ONLY public.author
    ADD CONSTRAINT author_pkey PRIMARY KEY (id);


--
-- Name: autobiografia autobiografia_author_id_key; Type: CONSTRAINT; Schema: public; Owner: zhyldyzbek
--

ALTER TABLE ONLY public.autobiografia
    ADD CONSTRAINT autobiografia_author_id_key UNIQUE (author_id);


--
-- Name: autobiografia autobiografia_pkey; Type: CONSTRAINT; Schema: public; Owner: zhyldyzbek
--

ALTER TABLE ONLY public.autobiografia
    ADD CONSTRAINT autobiografia_pkey PRIMARY KEY (id);


--
-- Name: blogger blogger_pkey; Type: CONSTRAINT; Schema: public; Owner: zhyldyzbek
--

ALTER TABLE ONLY public.blogger
    ADD CONSTRAINT blogger_pkey PRIMARY KEY (id);


--
-- Name: developer developer_pkey; Type: CONSTRAINT; Schema: public; Owner: zhyldyzbek
--

ALTER TABLE ONLY public.developer
    ADD CONSTRAINT developer_pkey PRIMARY KEY (id);


--
-- Name: post post_pkey; Type: CONSTRAINT; Schema: public; Owner: zhyldyzbek
--

ALTER TABLE ONLY public.post
    ADD CONSTRAINT post_pkey PRIMARY KEY (id);


--
-- Name: product2 product2_pkey; Type: CONSTRAINT; Schema: public; Owner: zhyldyzbek
--

ALTER TABLE ONLY public.product2
    ADD CONSTRAINT product2_pkey PRIMARY KEY (id);


--
-- Name: product product_pkey; Type: CONSTRAINT; Schema: public; Owner: zhyldyzbek
--

ALTER TABLE ONLY public.product
    ADD CONSTRAINT product_pkey PRIMARY KEY (id);


--
-- Name: project project_pkey; Type: CONSTRAINT; Schema: public; Owner: zhyldyzbek
--

ALTER TABLE ONLY public.project
    ADD CONSTRAINT project_pkey PRIMARY KEY (id);


--
-- Name: autobiografia fk_author_bio; Type: FK CONSTRAINT; Schema: public; Owner: zhyldyzbek
--

ALTER TABLE ONLY public.autobiografia
    ADD CONSTRAINT fk_author_bio FOREIGN KEY (author_id) REFERENCES public.author(id);


--
-- Name: dev_proj fk_dev; Type: FK CONSTRAINT; Schema: public; Owner: zhyldyzbek
--

ALTER TABLE ONLY public.dev_proj
    ADD CONSTRAINT fk_dev FOREIGN KEY (dev_id) REFERENCES public.developer(id);


--
-- Name: post fk_post_blogger; Type: FK CONSTRAINT; Schema: public; Owner: zhyldyzbek
--

ALTER TABLE ONLY public.post
    ADD CONSTRAINT fk_post_blogger FOREIGN KEY (blogger_id) REFERENCES public.blogger(id);


--
-- Name: dev_proj fk_proj; Type: FK CONSTRAINT; Schema: public; Owner: zhyldyzbek
--

ALTER TABLE ONLY public.dev_proj
    ADD CONSTRAINT fk_proj FOREIGN KEY (proj_id) REFERENCES public.project(id);


--
-- PostgreSQL database dump complete
--

