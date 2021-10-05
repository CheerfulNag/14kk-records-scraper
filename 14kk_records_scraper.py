import requests
import csv

def creating_csv():
    with open("results.csv","w",newline="",encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(['kenteken','voertuigsoort','Personenauto','merk','handelsbenaming','vervaldatum_apk','datum_tenaamstelling','bruto_bpm','inrichting','aantal_zitplaatsen','eerste_kleur','tweede_kleur','aantal_cilinders','cilinderinhoud','massa_ledig_voertuig','toegestane_maximum_massa_voertuig','massa_rijklaar','maximum_massa_trekken_ongeremd','maximum_trekken_massa_geremd','zuinigheidslabel','datum_eerste_toelating','datum_eerste_afgifte_nederland','wacht_op_keuren','catalogusprijs','wam_verzekerd','aantal_deuren','aantal_wielen','afstand_hart_koppeling_tot_achterzijde_voertuig','afstand_voorzijde_voertuig_tot_hart_koppeling','lengte','breedte','europese_voertuigcategorie','plaats_chassisnummer','technische_max_massa_voertuig','type','typegoedkeuringsnummer','variant','uitvoering','volgnummer_wijziging_eu_typegoedkeuring','vermogen_massarijklaar','wielbasis','export_indicator','openstaande_terugroepactie_indicator','taxi_indicator','maximum_massa_samenstelling','aantal_rolstoelplaatsen','maximum_ondersteunende_snelheid','jaar_laatste_registratie_tellerstand','tellerstandoordeel','code_toelichting_tellerstandoordeel','tenaamstellen_mogelijk','api_gekentekende_voertuigen_assen','api_gekentekende_voertuigen_brandstof','api_gekentekende_voertuigen_carrosserie','api_gekentekende_voertuigen_carrosserie_specifiek','api_gekentekende_voertuigen_voertuigklasse',':id'])

def adding_rows_to_csv():
    with open("results.csv","a",newline="",encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([x for x in records])

def main(limit = 14350000):
    print("Started")
    creating_csv()

    for x in range(0,limit,1000000):
        global records
        records = []
        x = str(x)
        querystring = {"$query":f"select *, :id offset {x} limit 1000000"}
        payload = ""
        r = requests.request("GET", url, data=payload, params=querystring)
        r = r.json()
        for item in r:
            record = []
            for key in keys:
                record.append(item.get(key))
            records.append(record)
        print(f"{int(x)+len(records)} records scraped")
        adding_rows_to_csv()


url = "https://opendata.rdw.nl/api/id/m9d7-ebf2.json"
keys = ['kenteken','voertuigsoort','merk','handelsbenaming','vervaldatum_apk','datum_tenaamstelling','bruto_bpm','inrichting','aantal_zitplaatsen','eerste_kleur','tweede_kleur','aantal_cilinders','cilinderinhoud','massa_ledig_voertuig','toegestane_maximum_massa_voertuig','massa_rijklaar','maximum_massa_trekken_ongeremd','maximum_trekken_massa_geremd','zuinigheidslabel','datum_eerste_toelating','datum_eerste_afgifte_nederland','wacht_op_keuren','catalogusprijs','wam_verzekerd','aantal_deuren','aantal_wielen','afstand_hart_koppeling_tot_achterzijde_voertuig','afstand_voorzijde_voertuig_tot_hart_koppeling','lengte','breedte','europese_voertuigcategorie','plaats_chassisnummer','technische_max_massa_voertuig','type','typegoedkeuringsnummer','variant','uitvoering','volgnummer_wijziging_eu_typegoedkeuring','vermogen_massarijklaar','wielbasis','export_indicator','openstaande_terugroepactie_indicator','taxi_indicator','maximum_massa_samenstelling','aantal_rolstoelplaatsen','maximum_ondersteunende_snelheid','jaar_laatste_registratie_tellerstand','tellerstandoordeel','code_toelichting_tellerstandoordeel','tenaamstellen_mogelijk','api_gekentekende_voertuigen_assen','api_gekentekende_voertuigen_brandstof','api_gekentekende_voertuigen_carrosserie','api_gekentekende_voertuigen_carrosserie_specifiek','api_gekentekende_voertuigen_voertuigklasse',':id']


main()

#Scraping will take about 60 minutes for 14.5kk results.
