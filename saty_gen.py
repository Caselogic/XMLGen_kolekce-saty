def generujObsah(hlavicka, paticka, nazev_zdroj, nazev_cil, i = 0):
	"Vygeneruje XML soubor pro FLASH na zaklade CSV souboru"

	# nacteni/vytvoreni pracovnich souboru 
	soubor_zdroj = file(nazev_zdroj, 'r')
	soubor_cil = file(nazev_cil,'a')

	# zapsani hlavicky na zacatek souboru
	soubor_cil.write(hlavicka)

	# cyklus prochazejici jednotlive radky souboru
	for radek in soubor_zdroj:	
		
		# vynechani 1. radku (hlavicky csv dokumentu)
		if i:		
			
			# zpracovani radku na jednotlive bunky
			csv_radek = str(radek)			
			csv_radek = csv_radek.strip()	
			csv = csv_radek.split(',')		
			
			
			# overeni zda-li nezpracovavame prazdny radek
			if len(csv[0]) > 1 and len(csv[2]) > 1 and len(csv[4]) > 1:	  	
				
				# tvorba tela dokumentu XML
				soubor_cil.write("\t<SATY>\n\t\t")
				
				soubor_cil.write('<MODEL>'+ csv[0].strip() +'</MODEL>\n\t\t')
				soubor_cil.write('<BARVA>'+ csv[1].strip() +'</BARVA>\n\t\t')
				soubor_cil.write('<CENA>'+ csv[2].strip() +'</CENA>\n\t\t')
				soubor_cil.write('<POPIS>'+ csv[3].strip() +'</POPIS>\n\t\t')
				soubor_cil.write('<ZDARMA>'+ csv[4].strip() +'</ZDARMA>\n\t')
				
				soubor_cil.write('</SATY>\n')
			
		i += 1

	# zapsani paticky na konec souboru
	soubor_cil.write(paticka)
	
	return



# definovani zdrojoveho souboru
nazev_zdroj = 'kolekce.csv'

# definovani ciloveho souboru
nazev_cil = 'katalog.xml'

# definovani hlavicky a paticky souboru
hlavicka = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<KATALOG xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">\n'
paticka = '</KATALOG>\n'
	
generujObsah(hlavicka, paticka, nazev_zdroj, nazev_cil)
