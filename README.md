--PKG
create or replace PACKAGE PKG_EXAMEN AS
v_experiencia NUMBER;
FUNCTION FN_ZONA_EXTREMA (p_zona_extrema NUMBER)RETURN NUMBER;
FUNCTION FN_RANKING(p_ranking NUMBER) RETURN NUMBER;

  /* TODO enter package declarations (types, exceptions, methods etc) here */ 

END PKG_EXAMEN;

--PKG BODY
create or replace PACKAGE BODY PKG_EXAMEN AS

   FUNCTION FN_ZONA_EXTREMA (p_zona_extrema NUMBER) RETURN NUMBER AS
    v_zona NUMBER;
  BEGIN
    BEGIN
      SELECT ptje_zona
      INTO v_zona
      FROM ptje_zona_extrema
      WHERE zona_extrema = p_zona_extrema;
    EXCEPTION
      WHEN NO_DATA_FOUND THEN
        v_zona := 0;
    END;
    
    RETURN v_zona;
  END FN_ZONA_EXTREMA;

  FUNCTION FN_RANKING (p_ranking NUMBER)RETURN NUMBER AS
  v_ranking NUMBER;
  BEGIN
  SELECT ptje_ranking
  INTO v_ranking
  FROM ptje_ranking_inst
  WHERE p_ranking BETWEEN rango_ranking_ini AND rango_ranking_ter;
    -- TAREA: Se necesita implantación para FUNCTION PKG_EXAMEN.FN_RANKING
    RETURN v_ranking;
  END FN_RANKING;

END PKG_EXAMEN;

--FUNCION ANNOS

create or replace FUNCTION FN_ANNOS_EXP(p_annos NUMBER) RETURN NUMBER AS
v_exp NUMBER;
BEGIN
BEGIN
SELECT ptje_experiencia
INTO v_exp
FROM ptje_annos_experiencia
WHERE p_annos BETWEEN rango_annos_ini AND rango_annos_ter;
EXCEPTION
      WHEN NO_DATA_FOUND THEN
        v_exp := 0;
END;
  RETURN v_exp;
END FN_ANNOS_EXP;

--FUNCION HORAS
create or replace FUNCTION FN_HORAS_TRABAJO(p_horas NUMBER) RETURN NUMBER AS 
v_horas NUMBER;
BEGIN
BEGIN
SELECT ptje_horas_trab
INTO v_horas
FROM ptje_horas_trabajo
WHERE p_horas BETWEEN rango_horas_ini AND rango_horas_ter;
  EXCEPTION
      WHEN NO_DATA_FOUND THEN
        v_horas := 0;
END;
  RETURN v_horas;
END FN_HORAS_TRABAJO;

--TRIGGER
create or replace TRIGGER TRG_RESULTADO_POSTULACION 
BEFORE INSERT ON detalle_puntaje_postulacion
FOR EACH ROW
DECLARE
v_final NUMBER;
v_resultado VARCHAR2(200);
BEGIN
v_final:= :NEW.ptje_annos_exp + :NEW.ptje_horas_trab +:NEW.ptje_zona_extrema + :NEW.ptje_ranking_inst;

IF v_final >= 4500 THEN v_resultado:='SELECCIONADO';
ELSE v_resultado:= 'NO SELECCIONADO';
END IF;


INSERT INTO resultado_postulacion
       VALUES(:NEW.run_postulante,v_final,v_resultado);
  NULL;
END;

--PROCEDIMIENTO
create or replace PROCEDURE SP_DETALLE_POSTULACION AS 
--CURSOR POSTULANTE
CURSOR cur_postulante IS
nt: +56 9 8190 9856 --v_experiencia:= EXTRACT(YEAR FROM SYSDATE) - EXTRACT(YEAR FROM reg_postulante.fecha_contrato);
nf: +56 9 4875 3446 --v_experiencia:= EXTRACT(YEAR FROM SYSDATE) - EXTRACT(YEAR FROM reg_postulante.fecha_contrato);
nc: +56 9 7355 0011 --pkg_examen.v_experiencia:=EXTRACT(YEAR FROM SYSDATE) - EXTRACT(YEAR FROM reg_postulante.fecha_contrato);
SELECT DISTINCT p.numrun,
       p.pnombre||' '||p.snombre||' '||p.apaterno||' '||p.amaterno nombre,
       s.zona_extrema,i.ranking,l.horas_semanales,l.fecha_contrato
FROM antecedentes_personales p JOIN antecedentes_laborales l ON p.numrun=l.numrun JOIN servicio_salud s ON l.cod_serv_salud = s.cod_serv_salud
                               JOIN postulacion_programa_espec pp ON p.numrun = pp.numrun JOIN programa_especializacion pe ON pp.cod_programa = pe.cod_programa
                               JOIN institucion i ON pe.cod_inst = i.cod_inst;
                               
        
--v_experiencia NUMBER;
BEGIN
--TRUNCAR
EXECUTE IMMEDIATE 'TRUNCATE TABLE detalle_puntaje_postulacion';

--LOOP
FOR reg_postulante IN cur_postulante LOOP

--PTJE EXPERIENCIA
--v_experiencia:= EXTRACT(YEAR FROM SYSDATE) - EXTRACT(YEAR FROM reg_postulante.fecha_contrato);
pkg_examen.v_experiencia:=EXTRACT(YEAR FROM SYSDATE) - EXTRACT(YEAR FROM reg_postulante.fecha_contrato);

BEGIN
INSERT INTO detalle_puntaje_postulacion
       VALUES(reg_postulante.numrun,reg_postulante.nombre,fn_annos_exp(pkg_examen.v_experiencia),fn_horas_trabajo(reg_postulante.horas_semanales),pkg_examen.fn_zona_extrema(reg_postulante.zona_extrema),pkg_examen.fn_ranking(reg_postulante.ranking),0,0);
EXCEPTION
            WHEN DUP_VAL_ON_INDEX THEN
                -- Manejo de duplicados en detalle_puntaje_postulacion
                NULL; -- Opcional: No hacer nada o registrar un mensaje de depuración
            WHEN OTHERS THEN
                -- Manejo de errores generales
                INSERT INTO error_proceso
                VALUES (reg_postulante.numrun, 'GENERAL_ERROR', 'Error en SP_DETALLE_POSTULACION');
        END;      
       
END LOOP;
--COMMIT
  
END SP_DETALLE_POSTULACION;




