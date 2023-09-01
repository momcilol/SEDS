CREATE MATERIALIZED VIEW MMW_KreditnaViabilnost AS
SELECT r.JMBG, r.ime, AVG(t.iznos) as prihod, 3 as meseci
FROM MMW_TRANSAKCIJA T, MMW_RACUN R, MMW_VREME V
WHERE t.vreme_idvreme = v.idvreme and t.racun_idracun = r.idracun
	and r.valuta = 'RSD'
	and v.godina = 2023 and v.mesecbr >= 6 and v.mesecbr <= 8
	and t.prihod = 1
GROUP BY r.JMBG, r.ime
UNION
SELECT r.JMBG, r.ime, AVG(t.iznos) as prihod, 6 as meseci
FROM MMW_TRANSAKCIJA T, MMW_RACUN R, MMW_VREME V
WHERE t.vreme_idvreme = v.idvreme and t.racun_idracun = r.idracun
	and r.valuta = 'RSD'
	and v.godina = 2023 and v.mesecbr >= 3 and v.mesecbr <= 8
	and t.prihod = 1
GROUP BY r.JMBG, r.ime
UNION
SELECT r.JMBG, r.ime, AVG(t.iznos) as prihod, 12 as meseci
FROM MMW_TRANSAKCIJA T, MMW_RACUN R, MMW_VREME V
WHERE t.vreme_idvreme = v.idvreme and t.racun_idracun = r.idracun
	and r.valuta = 'RSD'
	and v.datum BETWEEN TO_DATE('2022-08-31','YYYY-MM-DD') and TO_DATE('2023-09-01','YYYY-MM-DD')
	and t.prihod = 1
GROUP BY r.JMBG, r.ime;

SELECT JMBG, ime as "Ime i prezime", prihod as "Prosečan prihod", meseci as "Period", max(prihod) over (partition by JMBG) as max_prihod
FROM (  SELECT JMBG, ime, prihod, COUNT(*) over (partition by JMBG) as broj, meseci
    	FROM MMW_KreditnaViabilnost
    	WHERE prihod > 50000 )
WHERE broj = 3
ORDER BY max_prihod DESC, meseci;
