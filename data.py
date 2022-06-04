import streamlit as st
import pandas as pd
import csv
import graphviz as graphviz



my_data = pd.read_csv('lang_data.csv', usecols= ['name','latitude','longitude','genus','family'])
name_data_check = my_data['name']
name_data_check.to_csv('name_data.csv', sep=',')
with open('name_data.csv', 'r') as file:
	name_list = file.read()

languages = st.text_input("Language (use a comma to separate multiple languages):")


if languages:
	if ',' in languages:
		language_list = []
		coordinates = []
		fam_list = []
		genus_list = []
		languages = languages.split(",")
		for item in languages:
			item = item.strip()
			language_list.append(item)
		for language in language_list:
			if language in name_list:
				ss = my_data[my_data['name'] == language]
				coordinates.append([ss.iat[0,1],ss.iat[0,2]])
				fam = ss.iat[0,4]
				genus = ss.iat[0,3]
				fam_inf = (' '.join([language, " is a language of", fam, "family,", genus, "genus."]))
				st.caption(fam_inf)

				fam_list.append(fam)
				genus_list.append(genus)

			else:
				st.caption(' '.join([language, "not found. Check the spelling."]))

		graph = graphviz.Digraph()
		for i in range(len(fam_list)):
			graph.edge(fam_list[i], genus_list[i])
			graph.edge(genus_list[i], language_list[i])
		st.graphviz_chart(graph)

		df = pd.DataFrame(
			coordinates,
			columns=['lat', 'lon'])
		st.map(df)

	else:
		if languages in name_list:
			ss = my_data[my_data['name'] == languages]
			fam = ss.iat[0,4]
			genus = ss.iat[0,3]
			fam_inf = (' '.join([languages, " is a language of", fam, "family,", genus, "genus."]))
			st.caption(fam_inf)

			graph = graphviz.Digraph()
			graph.edge(fam, genus)
			graph.edge(genus, languages)
			st.graphviz_chart(graph)

			lat = ss.latitude.to_list()
			lon = ss.longitude.to_list()
			df = pd.DataFrame({"lat":lat, "lon":lon})
			st.map(df)
		else:
			st.caption(' '.join([languages, "not found. Check the spelling."]))

