import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')

figure.write_html('ventes-par-region.html')

print('ventes-par-région.html généré avec succès !')
ventes_par_produit = données.groupby('produit', as_index=False)['qte'].sum()
print(ventes_par_produit)
figure_produit = px.bar(ventes_par_produit, x='produit', y='qte', title='Quantité vendue par produit')
figure_produit.write_html('ventes-par-produit.html')
données['chiffre_affaires'] = données['prix'] * données['qte']
ca_par_produit = données.groupby('produit', as_index=False)['chiffre_affaires'].sum()
print(ca_par_produit)
figure_ca = px.bar(ca_par_produit, x='produit', y='chiffre_affaires', title="Chiffre d'affaires par produit")
figure_ca.write_html('chiffre-affaires-par-produit.html')