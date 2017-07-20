--
-- PostgreSQL database dump
--

-- Dumped from database version 9.4.3
-- Dumped by pg_dump version 9.4.3
-- Started on 2015-09-11 16:30:38 VET

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET search_path = public, pg_catalog;

--
-- TOC entry 2205 (class 0 OID 25108)
-- Dependencies: 172
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 2244 (class 0 OID 0)
-- Dependencies: 173
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_group_id_seq', 1, false);


--
-- TOC entry 2219 (class 0 OID 25147)
-- Dependencies: 186
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO django_content_type (id, name, app_label, model) VALUES (1, 'log entry', 'admin', 'logentry');
INSERT INTO django_content_type (id, name, app_label, model) VALUES (2, 'permission', 'auth', 'permission');
INSERT INTO django_content_type (id, name, app_label, model) VALUES (3, 'group', 'auth', 'group');
INSERT INTO django_content_type (id, name, app_label, model) VALUES (4, 'user', 'auth', 'user');
INSERT INTO django_content_type (id, name, app_label, model) VALUES (5, 'content type', 'contenttypes', 'contenttype');
INSERT INTO django_content_type (id, name, app_label, model) VALUES (6, 'session', 'sessions', 'session');
INSERT INTO django_content_type (id, name, app_label, model) VALUES (7, 'tipo educacion', 'tipo_educacion', 'tipoeducacion');
INSERT INTO django_content_type (id, name, app_label, model) VALUES (8, 'grados', 'grados', 'grados');
INSERT INTO django_content_type (id, name, app_label, model) VALUES (9, 'modelos', 'modelos', 'modelos');
INSERT INTO django_content_type (id, name, app_label, model) VALUES (10, 'estado', 'estados', 'estado');
INSERT INTO django_content_type (id, name, app_label, model) VALUES (11, 'municipio', 'municipios', 'municipio');
INSERT INTO django_content_type (id, name, app_label, model) VALUES (12, 'parroquia', 'parroquias', 'parroquia');
INSERT INTO django_content_type (id, name, app_label, model) VALUES (13, 'estudiante', 'estudiante', 'estudiante');
INSERT INTO django_content_type (id, name, app_label, model) VALUES (14, 'representante', 'representante', 'representante');


--
-- TOC entry 2209 (class 0 OID 25118)
-- Dependencies: 176
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (4, 'Can add permission', 2, 'add_permission');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (5, 'Can change permission', 2, 'change_permission');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (6, 'Can delete permission', 2, 'delete_permission');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (7, 'Can add group', 3, 'add_group');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (8, 'Can change group', 3, 'change_group');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (9, 'Can delete group', 3, 'delete_group');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (10, 'Can add user', 4, 'add_user');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (11, 'Can change user', 4, 'change_user');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (12, 'Can delete user', 4, 'delete_user');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (13, 'Can add content type', 5, 'add_contenttype');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (14, 'Can change content type', 5, 'change_contenttype');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (15, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (16, 'Can add session', 6, 'add_session');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (17, 'Can change session', 6, 'change_session');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (18, 'Can delete session', 6, 'delete_session');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (19, 'Can add tipo educacion', 7, 'add_tipoeducacion');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (20, 'Can change tipo educacion', 7, 'change_tipoeducacion');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (21, 'Can delete tipo educacion', 7, 'delete_tipoeducacion');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (22, 'Can add grados', 8, 'add_grados');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (23, 'Can change grados', 8, 'change_grados');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (24, 'Can delete grados', 8, 'delete_grados');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (25, 'Can add modelos', 9, 'add_modelos');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (26, 'Can change modelos', 9, 'change_modelos');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (27, 'Can delete modelos', 9, 'delete_modelos');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (28, 'Can add estado', 10, 'add_estado');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (29, 'Can change estado', 10, 'change_estado');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (30, 'Can delete estado', 10, 'delete_estado');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (31, 'Can add municipio', 11, 'add_municipio');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (32, 'Can change municipio', 11, 'change_municipio');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (33, 'Can delete municipio', 11, 'delete_municipio');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (34, 'Can add parroquia', 12, 'add_parroquia');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (35, 'Can change parroquia', 12, 'change_parroquia');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (36, 'Can delete parroquia', 12, 'delete_parroquia');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (37, 'Can add estudiante', 13, 'add_estudiante');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (38, 'Can change estudiante', 13, 'change_estudiante');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (39, 'Can delete estudiante', 13, 'delete_estudiante');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (40, 'Can add representante', 14, 'add_representante');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (41, 'Can change representante', 14, 'change_representante');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (42, 'Can delete representante', 14, 'delete_representante');


--
-- TOC entry 2207 (class 0 OID 25113)
-- Dependencies: 174
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 2245 (class 0 OID 0)
-- Dependencies: 175
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 1, false);


--
-- TOC entry 2246 (class 0 OID 0)
-- Dependencies: 177
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_permission_id_seq', 42, true);


--
-- TOC entry 2211 (class 0 OID 25123)
-- Dependencies: 178
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (1, 'pbkdf2_sha256$15000$P8bnodunfUxp$7OdRv7h7tkh57+YyBSqprGlHEHkLR9Un6V3Ti8KqxW8=', '2015-09-05 17:28:37.020471-04:30', true, 'admin', '', '', '', true, true, '2015-09-05 17:28:37.020471-04:30');


--
-- TOC entry 2212 (class 0 OID 25126)
-- Dependencies: 179
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 2247 (class 0 OID 0)
-- Dependencies: 180
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_user_groups_id_seq', 1, false);


--
-- TOC entry 2248 (class 0 OID 0)
-- Dependencies: 181
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_user_id_seq', 1, true);


--
-- TOC entry 2215 (class 0 OID 25133)
-- Dependencies: 182
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 2249 (class 0 OID 0)
-- Dependencies: 183
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);


--
-- TOC entry 2217 (class 0 OID 25138)
-- Dependencies: 184
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 2250 (class 0 OID 0)
-- Dependencies: 185
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 1, false);


--
-- TOC entry 2251 (class 0 OID 0)
-- Dependencies: 187
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('django_content_type_id_seq', 14, true);


--
-- TOC entry 2221 (class 0 OID 25152)
-- Dependencies: 188
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO django_migrations (id, app, name, applied) VALUES (1, 'contenttypes', '0001_initial', '2015-09-05 17:28:14.139658-04:30');
INSERT INTO django_migrations (id, app, name, applied) VALUES (2, 'auth', '0001_initial', '2015-09-05 17:28:14.925212-04:30');
INSERT INTO django_migrations (id, app, name, applied) VALUES (3, 'admin', '0001_initial', '2015-09-05 17:28:15.133321-04:30');
INSERT INTO django_migrations (id, app, name, applied) VALUES (4, 'sessions', '0001_initial', '2015-09-05 17:28:15.29184-04:30');
INSERT INTO django_migrations (id, app, name, applied) VALUES (5, 'tipo_educacion', '0001_initial', '2015-09-05 17:29:20.416463-04:30');
INSERT INTO django_migrations (id, app, name, applied) VALUES (6, 'grados', '0001_initial', '2015-09-05 17:40:38.144861-04:30');
INSERT INTO django_migrations (id, app, name, applied) VALUES (7, 'modelos', '0001_initial', '2015-09-05 17:40:38.213066-04:30');
INSERT INTO django_migrations (id, app, name, applied) VALUES (8, 'estados', '0001_initial', '2015-09-07 11:38:14.935465-04:30');
INSERT INTO django_migrations (id, app, name, applied) VALUES (10, 'parroquias', '0001_initial', '2015-09-07 14:46:40.732343-04:30');
INSERT INTO django_migrations (id, app, name, applied) VALUES (12, 'municipios', '0001_initial', '2015-09-09 15:06:05.712043-04:30');
INSERT INTO django_migrations (id, app, name, applied) VALUES (13, 'estudiante', '0001_initial', '2015-09-09 15:57:14.8122-04:30');
INSERT INTO django_migrations (id, app, name, applied) VALUES (14, 'representante', '0001_initial', '2015-09-11 14:45:05.778662-04:30');


--
-- TOC entry 2252 (class 0 OID 0)
-- Dependencies: 189
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('django_migrations_id_seq', 14, true);


--
-- TOC entry 2223 (class 0 OID 25160)
-- Dependencies: 190
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 2231 (class 0 OID 25300)
-- Dependencies: 198
-- Data for Name: estados_estado; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO estados_estado (id, cod_estado, estado, "user", date_create, date_update) VALUES (10, 1, 'DISTRITO CAPITAL', NULL, NULL, NULL);
INSERT INTO estados_estado (id, cod_estado, estado, "user", date_create, date_update) VALUES (11, 2, 'ANZOATEGUI', NULL, NULL, NULL);
INSERT INTO estados_estado (id, cod_estado, estado, "user", date_create, date_update) VALUES (12, 3, 'APURE', NULL, NULL, NULL);
INSERT INTO estados_estado (id, cod_estado, estado, "user", date_create, date_update) VALUES (13, 4, 'ARAGUA', NULL, NULL, NULL);
INSERT INTO estados_estado (id, cod_estado, estado, "user", date_create, date_update) VALUES (14, 5, 'BARINAS', NULL, NULL, NULL);
INSERT INTO estados_estado (id, cod_estado, estado, "user", date_create, date_update) VALUES (15, 6, 'BOLIVAR', NULL, NULL, NULL);
INSERT INTO estados_estado (id, cod_estado, estado, "user", date_create, date_update) VALUES (16, 7, 'CARABOBO', NULL, NULL, NULL);
INSERT INTO estados_estado (id, cod_estado, estado, "user", date_create, date_update) VALUES (17, 8, 'COJEDES', NULL, NULL, NULL);
INSERT INTO estados_estado (id, cod_estado, estado, "user", date_create, date_update) VALUES (18, 9, 'FALCON', NULL, NULL, NULL);
INSERT INTO estados_estado (id, cod_estado, estado, "user", date_create, date_update) VALUES (19, 10, 'GUARICO', NULL, NULL, NULL);
INSERT INTO estados_estado (id, cod_estado, estado, "user", date_create, date_update) VALUES (20, 11, 'LARA', NULL, NULL, NULL);
INSERT INTO estados_estado (id, cod_estado, estado, "user", date_create, date_update) VALUES (21, 12, 'MERIDA', NULL, NULL, NULL);
INSERT INTO estados_estado (id, cod_estado, estado, "user", date_create, date_update) VALUES (22, 13, 'MIRANDA', NULL, NULL, NULL);
INSERT INTO estados_estado (id, cod_estado, estado, "user", date_create, date_update) VALUES (23, 14, 'MONAGAS', NULL, NULL, NULL);
INSERT INTO estados_estado (id, cod_estado, estado, "user", date_create, date_update) VALUES (24, 15, 'NUEVA ESPARTA', NULL, NULL, NULL);
INSERT INTO estados_estado (id, cod_estado, estado, "user", date_create, date_update) VALUES (25, 16, 'PORTUGUESA', NULL, NULL, NULL);
INSERT INTO estados_estado (id, cod_estado, estado, "user", date_create, date_update) VALUES (26, 17, 'SUCRE', NULL, NULL, NULL);
INSERT INTO estados_estado (id, cod_estado, estado, "user", date_create, date_update) VALUES (27, 18, 'TACHIRA', NULL, NULL, NULL);
INSERT INTO estados_estado (id, cod_estado, estado, "user", date_create, date_update) VALUES (28, 19, 'TRUJILLO', NULL, NULL, NULL);
INSERT INTO estados_estado (id, cod_estado, estado, "user", date_create, date_update) VALUES (29, 20, 'YARACUY', NULL, NULL, NULL);
INSERT INTO estados_estado (id, cod_estado, estado, "user", date_create, date_update) VALUES (30, 21, 'ZULIA', NULL, NULL, NULL);
INSERT INTO estados_estado (id, cod_estado, estado, "user", date_create, date_update) VALUES (31, 22, 'AMAZONAS', NULL, NULL, NULL);
INSERT INTO estados_estado (id, cod_estado, estado, "user", date_create, date_update) VALUES (32, 23, 'DELTA AMACURO', NULL, NULL, NULL);
INSERT INTO estados_estado (id, cod_estado, estado, "user", date_create, date_update) VALUES (33, 24, 'VARGAS', NULL, NULL, NULL);


--
-- TOC entry 2253 (class 0 OID 0)
-- Dependencies: 197
-- Name: estados_estado_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('estados_estado_id_seq', 33, true);


--
-- TOC entry 2228 (class 0 OID 25176)
-- Dependencies: 195
-- Data for Name: tipo_educacion_tipoeducacion; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO tipo_educacion_tipoeducacion (id, tipo) VALUES (8, 'bsca');
INSERT INTO tipo_educacion_tipoeducacion (id, tipo) VALUES (9, 'yooooo');
INSERT INTO tipo_educacion_tipoeducacion (id, tipo) VALUES (10, 'dfgdg');
INSERT INTO tipo_educacion_tipoeducacion (id, tipo) VALUES (11, 'dffsfs');


--
-- TOC entry 2224 (class 0 OID 25166)
-- Dependencies: 191
-- Data for Name: grados_grados; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO grados_grados (id, grado, tipo_id) VALUES (7, 'esteee', 11);
INSERT INTO grados_grados (id, grado, tipo_id) VALUES (11, 'ggggggggggggggggggg', 9);


--
-- TOC entry 2237 (class 0 OID 25366)
-- Dependencies: 204
-- Data for Name: estudiante_estudiante; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO estudiante_estudiante (id, codigo, usuario, fecha_s, fecha_e, nombre, apellido, sexo, edad, escuela, parroquia, municipio, direcc_es, estado_id, grado_id, tipo_id) VALUES (2, '1', 'xfgf', '2015-09-10 14:43:50.191658-04:30', '2015-09-10 14:43:50.191745-04:30', 'fgf', 'xfgf', 'fxfg', 10, 'hfhdf', 5, 3, 'dfgdfg', 13, 7, 8);
INSERT INTO estudiante_estudiante (id, codigo, usuario, fecha_s, fecha_e, nombre, apellido, sexo, edad, escuela, parroquia, municipio, direcc_es, estado_id, grado_id, tipo_id) VALUES (3, '2', 'h', '2015-09-10 15:25:18.260913-04:30', '2015-09-10 15:25:18.261063-04:30', 'hghgf', 'gfhfg', 'gf', 15, 'ghfg', 4, 6, 'lljl', 13, 11, 8);
INSERT INTO estudiante_estudiante (id, codigo, usuario, fecha_s, fecha_e, nombre, apellido, sexo, edad, escuela, parroquia, municipio, direcc_es, estado_id, grado_id, tipo_id) VALUES (4, '1', 'fdf', '2015-09-11 08:39:08.772031-04:30', '2015-09-11 08:39:08.772764-04:30', 'fdsf', 'fdsf', 'dsfds', 8, 'fdsfds', 3, 3, 'fsdfdsfsd', 13, 7, 8);
INSERT INTO estudiante_estudiante (id, codigo, usuario, fecha_s, fecha_e, nombre, apellido, sexo, edad, escuela, parroquia, municipio, direcc_es, estado_id, grado_id, tipo_id) VALUES (5, '5', 'hkuh', '2015-09-11 08:44:01.950834-04:30', '2015-09-11 08:44:01.9509-04:30', 'hkhjkl', 'hkujhjk', 'hjkhjk', 10, 'hyuihio', 4, 4, 'huihjkhjkhkj			', 13, 11, 10);
INSERT INTO estudiante_estudiante (id, codigo, usuario, fecha_s, fecha_e, nombre, apellido, sexo, edad, escuela, parroquia, municipio, direcc_es, estado_id, grado_id, tipo_id) VALUES (6, '6', 'hkjhk', '2015-09-11 08:50:04.392524-04:30', '2015-09-11 08:50:04.392585-04:30', 'hjkh', 'hjk', 'hjkh', 14, 'jhkjh', 2, 2, 'hukjhjkhj', 13, 7, 8);
INSERT INTO estudiante_estudiante (id, codigo, usuario, fecha_s, fecha_e, nombre, apellido, sexo, edad, escuela, parroquia, municipio, direcc_es, estado_id, grado_id, tipo_id) VALUES (7, '7', 'hjkh', '2015-09-11 09:14:13.536638-04:30', '2015-09-11 09:14:13.536706-04:30', 'hjkh', 'hjkhj', 'hjkhjk', 10, 'jkljl', 3, 3, 'jijiljio', 13, 7, 8);
INSERT INTO estudiante_estudiante (id, codigo, usuario, fecha_s, fecha_e, nombre, apellido, sexo, edad, escuela, parroquia, municipio, direcc_es, estado_id, grado_id, tipo_id) VALUES (8, '8', 'hjkh', '2015-09-11 09:18:44.576958-04:30', '2015-09-11 09:18:44.577021-04:30', 'hjkh', 'hjkh', 'hjkhk', 12, 'hjkhjk', 3, 3, 'hjkhjkhjk', 13, 7, 9);


--
-- TOC entry 2254 (class 0 OID 0)
-- Dependencies: 203
-- Name: estudiante_estudiante_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('estudiante_estudiante_id_seq', 16, true);


--
-- TOC entry 2255 (class 0 OID 0)
-- Dependencies: 192
-- Name: grados_grados_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('grados_grados_id_seq', 11, true);


--
-- TOC entry 2226 (class 0 OID 25171)
-- Dependencies: 193
-- Data for Name: modelos_modelos; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO modelos_modelos (id, nombre) VALUES (1, 'jujujjj');
INSERT INTO modelos_modelos (id, nombre) VALUES (5, 'gggggggggggggg');


--
-- TOC entry 2256 (class 0 OID 0)
-- Dependencies: 194
-- Name: modelos_modelos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('modelos_modelos_id_seq', 7, true);


--
-- TOC entry 2235 (class 0 OID 25352)
-- Dependencies: 202
-- Data for Name: municipios_municipio; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO municipios_municipio (id, municipio, cod_municipio, date_create, date_update, "user", estado_id) VALUES (6, 'GIRARDOT', 1, NULL, NULL, NULL, 4);
INSERT INTO municipios_municipio (id, municipio, cod_municipio, date_create, date_update, "user", estado_id) VALUES (7, 'SANTIAGO MARIÑO', 2, NULL, NULL, NULL, 4);
INSERT INTO municipios_municipio (id, municipio, cod_municipio, date_create, date_update, "user", estado_id) VALUES (8, 'JOSE FELIX RIBAS', 3, NULL, NULL, NULL, 4);
INSERT INTO municipios_municipio (id, municipio, cod_municipio, date_create, date_update, "user", estado_id) VALUES (9, 'SAN CASIMIRO', 4, NULL, NULL, NULL, 4);
INSERT INTO municipios_municipio (id, municipio, cod_municipio, date_create, date_update, "user", estado_id) VALUES (10, 'SAN SEBASTIAN', 5, NULL, NULL, NULL, 4);
INSERT INTO municipios_municipio (id, municipio, cod_municipio, date_create, date_update, "user", estado_id) VALUES (11, 'SUCRE', 6, NULL, NULL, NULL, 4);
INSERT INTO municipios_municipio (id, municipio, cod_municipio, date_create, date_update, "user", estado_id) VALUES (12, 'URDANETA', 7, NULL, NULL, NULL, 4);
INSERT INTO municipios_municipio (id, municipio, cod_municipio, date_create, date_update, "user", estado_id) VALUES (13, 'ZAMORA', 8, NULL, NULL, NULL, 4);
INSERT INTO municipios_municipio (id, municipio, cod_municipio, date_create, date_update, "user", estado_id) VALUES (14, 'LIBERTADOS', 9, NULL, NULL, NULL, 4);
INSERT INTO municipios_municipio (id, municipio, cod_municipio, date_create, date_update, "user", estado_id) VALUES (15, 'JOSE ANGEL LAMAS', 10, NULL, NULL, NULL, 4);
INSERT INTO municipios_municipio (id, municipio, cod_municipio, date_create, date_update, "user", estado_id) VALUES (16, 'BOLIVAR', 11, NULL, NULL, NULL, 4);
INSERT INTO municipios_municipio (id, municipio, cod_municipio, date_create, date_update, "user", estado_id) VALUES (17, 'SANTOS MICHELENA', 12, NULL, NULL, NULL, 4);
INSERT INTO municipios_municipio (id, municipio, cod_municipio, date_create, date_update, "user", estado_id) VALUES (18, 'MARIO BRICEÑO IRAGORRY', 13, NULL, NULL, NULL, 4);
INSERT INTO municipios_municipio (id, municipio, cod_municipio, date_create, date_update, "user", estado_id) VALUES (19, 'TOVAR', 14, NULL, NULL, NULL, 4);
INSERT INTO municipios_municipio (id, municipio, cod_municipio, date_create, date_update, "user", estado_id) VALUES (20, 'CAMATAGUA', 15, NULL, NULL, NULL, 4);
INSERT INTO municipios_municipio (id, municipio, cod_municipio, date_create, date_update, "user", estado_id) VALUES (21, 'JOSE RAFAEL REVENGA', 16, NULL, NULL, NULL, 4);
INSERT INTO municipios_municipio (id, municipio, cod_municipio, date_create, date_update, "user", estado_id) VALUES (22, 'FRANCISCO LINARES ALCANTARA', 17, NULL, NULL, NULL, 4);
INSERT INTO municipios_municipio (id, municipio, cod_municipio, date_create, date_update, "user", estado_id) VALUES (23, 'OCUMARE DE LA COSTA', 18, NULL, NULL, NULL, 4);


--
-- TOC entry 2257 (class 0 OID 0)
-- Dependencies: 201
-- Name: municipios_municipio_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('municipios_municipio_id_seq', 23, true);


--
-- TOC entry 2233 (class 0 OID 25324)
-- Dependencies: 200
-- Data for Name: parroquias_parroquia; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (21, 'ANDRÉS ELOY BLANCO', 7, 1, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (22, 'CHORONI', 2, 1, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (23, 'JOAQUIN CRESPO', 4, 1, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (24, 'JOSÉ CASANOVA GODOY', 6, 1, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (25, 'LAS DELICIAS', 1, 1, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (26, 'LOS TACARIGUAS', 8, 1, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (27, 'MADRE MARÍA DE SAN JOSÉ', 3, 1, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (28, 'PEDRO JOSÉ OVALLES', 5, 1, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (29, 'SAN MATEO', 1, 11, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (30, 'CAMATAGUA', 1, 15, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (31, 'CARMEN DE CURA', 2, 15, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (32, 'SANTA RITA', 1, 17, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (33, 'FRANCISCO DE MIRANDA', 2, 17, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (34, 'MONSEÑOR FELICIANO GONZALÉZ', 3, 17, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (35, 'SANTA CRUZ', 1, 10, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (36, 'JUAN VICENTE BOLÍVAR', 1, 3, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (37, 'CASTOR NIEVES RÍOS', 4, 3, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (38, 'LAS GUACAMAYAS', 5, 3, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (39, 'PAO DE ZARATE', 3, 3, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (40, 'ZUATA', 2, 3, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (41, 'EL CONSEJO', 1, 16, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (42, 'PALO NEGRO', 1, 9, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (43, 'SAN MARTÍN DE PORRES', 2, 9, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (44, 'EL LIMÓN', 1, 13, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (45, 'CAÑA DE AZUCAR', 2, 13, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (46, 'OCUMARE DE LA COSTA', 1, 18, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (47, 'SAN CASIMIRO', 1, 4, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (48, 'GÜIRIPA', 3, 4, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (49, 'OLLAS DE CARAMACATE', 4, 4, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (50, 'VALLE MORÍN', 2, 4, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (51, 'SAN SEBASTIAN', 1, 5, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (52, 'TURMERO', 1, 2, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (53, 'ALFREDO PACHECO MIRANDA', 3, 2, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (54, 'AREVALO APONTE', 5, 2, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (55, 'CHUAO', 4, 2, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (56, 'SAMAN DE GÜERE', 2, 2, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (57, 'LAS TEJERÍAS', 1, 12, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (58, 'TIARA', 2, 12, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (59, 'CAGUA', 1, 6, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (60, 'BELLA VISTA', 2, 6, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (61, 'COLONIA TOVAR', 1, 14, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (62, 'BARBACOAS', 1, 7, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (63, 'LAS PEÑITAS', 4, 7, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (64, 'SAN FRANCISCO DE CARA', 2, 7, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (65, 'TAGUAY', 3, 7, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (66, 'VILLA DE CURA', 1, 8, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (67, 'MAGDALENO', 2, 8, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (68, 'AUGUSTO MIJARES', 5, 8, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (69, 'SAN FRANCISCO DE ASIS', 3, 8, NULL, NULL, NULL, 4);
INSERT INTO parroquias_parroquia (id, parroquia, cod_parroquia, municipio, "user", date_create, date_update, estado_id) VALUES (70, 'VALLES DE TUCUTUNEMO', 4, 8, NULL, NULL, NULL, 4);


--
-- TOC entry 2258 (class 0 OID 0)
-- Dependencies: 199
-- Name: parroquias_parroquia_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('parroquias_parroquia_id_seq', 70, true);


--
-- TOC entry 2239 (class 0 OID 25411)
-- Dependencies: 206
-- Data for Name: representante_representante; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO representante_representante (id, cedula, nombre, apellido, telefono1, telefono2, email, municipio, parroquia, direcc_re, estado_id) VALUES (1, 17703240, 'gdfg', 'dfghdfg', 2, 2, 'sfgsdgdfg@hotmail.com', 2, 2, 'holaaaaaaaaaaaa', 13);


--
-- TOC entry 2259 (class 0 OID 0)
-- Dependencies: 205
-- Name: representante_representante_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('representante_representante_id_seq', 3, true);


--
-- TOC entry 2260 (class 0 OID 0)
-- Dependencies: 196
-- Name: tipo_educacion_tipoeducacion_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('tipo_educacion_tipoeducacion_id_seq', 12, true);


-- Completed on 2015-09-11 16:30:38 VET

--
-- PostgreSQL database dump complete
--

