-- criar_tabela.sql · DataSUSpeitos (FMU Tech Inovação 2026.2 · ODS 3)
-- Cria a tabela final do projeto: uma linha por município de SP × ano.
-- Banco: PostgreSQL. As regras abaixo fazem o próprio banco recusar dados impossíveis.

CREATE TABLE IF NOT EXISTS fato_municipio_ano (
    cod_ibge                 CHAR(6)      NOT NULL,  -- código IBGE do município, como texto
    municipio                VARCHAR(100) NOT NULL,  -- nome do município (com acento)
    ano                      SMALLINT     NOT NULL,  -- ano do nascimento / da notificação
    nascidos_vivos           INTEGER      NOT NULL CHECK (nascidos_vivos >= 0),
    nv_consultas_informadas  INTEGER      NOT NULL CHECK (nv_consultas_informadas >= 0),
    nv_menos_7_consultas     INTEGER      NOT NULL CHECK (nv_menos_7_consultas >= 0),
    casos_sc                 INTEGER      NOT NULL CHECK (casos_sc >= 0),
    casos_sc_diag_prenatal   INTEGER      NOT NULL CHECK (casos_sc_diag_prenatal >= 0),
    elegivel_ranking         BOOLEAN      NOT NULL,  -- verdadeiro se nascidos_vivos >= 1000 no ano

    -- Chave primária: o mesmo município não pode aparecer duas vezes no mesmo ano
    CONSTRAINT pk_fato_municipio_ano PRIMARY KEY (cod_ibge, ano),

    -- Regras de coerência entre as colunas (as mesmas que o tratamento.py confere)
    CONSTRAINT ck_consultas  CHECK (nv_menos_7_consultas <= nv_consultas_informadas
                                    AND nv_consultas_informadas <= nascidos_vivos),
    CONSTRAINT ck_diagnostico CHECK (casos_sc_diag_prenatal <= casos_sc)
);
