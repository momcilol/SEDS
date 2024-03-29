SELECT VALUTA as "Valuta", OK.NAZIV as "Okrug", SUM(IZNOS) AS "Iznos", 
	SUM(BROJTRANSAKCIJA) AS "Broj transakcija", 
	SUM(SUM(BROJTRANSAKCIJA)) over (PARTITION BY VALUTA) AS "Broj transakcija valuta"
FROM 
	(SELECT R.VALUTA, B.NASELJE_IDNASELJE as IDNASELJE,
	SUM(ABS(T.IZNOS)) AS IZNOS, SUM(T.BROJTRANSAKCIJA) AS BROJTRANSAKCIJA
	FROM MMW_TRANSAKCIJA T, MMW_RACUN R, MMW_BANKOMAT B, MMW_VREME V
	WHERE V.GODINA = 2022 and t.racun_idracun = r.idracun
		and T.BANKOMAT_IDBANKOMAT = B.IDBANKOMAT
		and V.IDVREME = T.VREME_IDVREME
	GROUP BY R.VALUTA, B.NASELJE_IDNASELJE
	UNION
	SELECT R.VALUTA, E.NASELJE_IDNASELJE AS IDNASELJE, 
		SUM(ABS(T.IZNOS)) AS IZNOS, 
		SUM(T.BROJTRANSAKCIJA) AS BROJTRANSAKCIJA
	FROM MMW_TRANSAKCIJA T, MMW_RACUN R, MMW_EKSPOZITURA E , MMW_VREME V
	WHERE V.GODINA = 2022 and t.racun_idracun = r.idracun
		and T.EKSPOZITURA_IDEKSPOZITURA = E.IDEKSPOZITURA
		and V.IDVREME = T.VREME_IDVREME
	GROUP BY E.NASELJE_IDNASELJE, R.VALUTA) BE,
	MMW_NASELJE NA, MMW_OPSTINA OP, MMW_OKRUG OK
WHERE BE.IDNASELJE = NA.IDNASELJE AND NA.OPSTINA_IDOPSTINA = OP.IDOPSTINA
	AND OP.OKRUG_IDOKRUG = OK.IDOKRUG
GROUP BY VALUTA, OK.NAZIV
ORDER BY VALUTA, OK.NAZIV
