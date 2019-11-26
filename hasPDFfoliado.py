# -*- encoding: utf-8 -*-
import subprocess
import codecs
import pymysql


    
    
cnx = pymysql.connect(user='root', password='Showthebytes2113.', host='132.247.90.106', database='cadena_custodia')

cursor = cnx.cursor()


q = "SELECT * from usuarios"
cursor.execute(q)

for row in cursor:
    print (row[3])

pluma = codecs.open ("pytesttex.tex", "w", 'utf-8')
 
pluma.write(r'\documentclass{article}' + '\n')
pluma.write(r'\usepackage[utf8]{inputenc}' + '\n')
pluma.write(r'\usepackage{graphicx}' + '\n')
pluma.write(r'\usepackage{booktabs}' + '\n')
pluma.write(r'\usepackage{array}' + '\n')
pluma.write(r'\newcolumntype{M}[1]{>{\centering\arraybackslash}m{#1}}' + '\n')
pluma.write(r'\newcolumntype{N}{@{}m{0pt}@{}}' + '\n')
pluma.write(r'\usepackage[utf8]{inputenc}' + '\n')
pluma.write(r'\usepackage{graphicx}' + '\n')
pluma.write(r'\usepackage[usenames,dvipsnames,table]{xcolor}' + '\n')
pluma.write(r'\usepackage{geometry}' + '\n')
pluma.write(r'\setlength{\arrayrulewidth}{0.5mm}' + '\n')
pluma.write(r'\setlength{\tabcolsep}{10pt}' + '\n')
pluma.write(r'\renewcommand{\arraystretch}{1.5}' + '\n')
pluma.write(r'\geometry{' + '\n')
pluma.write(r' a4paper,' + '\n')
pluma.write(r' left=0mm,' + '\n')
pluma.write(r' right=0mm,' + '\n')
pluma.write(r' top=0mm,' + '\n')
pluma.write(r' bottom=0mm,' + '\n')
pluma.write(r' hoffset=0mm' + '\n')
pluma.write(r'}' + '\n')
pluma.write(r'\usepackage{array}' + '\n')
pluma.write(r'\newcolumntype{M}[1]{>{\centering\arraybackslash}m{#1}}' + '\n')
pluma.write(r'\newcolumntype{N}{@{}m{0pt}@{}}' + '\n')
pluma.write(r'\definecolor{gainsboro}{rgb}{0.86, 0.86, 0.86}' + '\n')
 
pluma.write(r'\begin{document}' + '\n')
pluma.write(r'\begin{center}' + '\n')
     
pluma.write(r'    \includegraphics{encabezado.png}' + '\n')
 
pluma.write(r'     \begin{tabular}{ | p{7cm} | p{3.5cm} | p{7cm} |}' + '\n')
pluma.write(r'    \hline' + '\n')
pluma.write(r'    Folio : {\color{red}LANCIS-PCR-FCC-I0001/2015} & Fecha : 21/06/2015 & Observaciones \\     \hline' + '\n')
     
pluma.write(r'    \multicolumn{2}{|p{10.5cm}|}{\textbf{Universidad Nacional Autónoma de México }\newline' + '\n') 
pluma.write(r'    Av. Universidad 3000, Col. UNAM, CU, Del. Coyoacán, CP 04510}' + '\n')
 
     
     
pluma.write(r'     &  \\     \hline' + '\n')
     
     
pluma.write(r'    \end{tabular}' + '\n')
     
pluma.write(r'    \begin{tabular}{ | p{9.1cm} | p{9.1cm} |}' + '\n')
pluma.write(r'    \hline' + '\n')
pluma.write(r'    \multicolumn{2}{|p{18.2cm}|}{Proyecto : Derrame minero en el río Sonora, evaluación ambiental}\\' + '\n')
pluma.write(r'    \hline' + '\n')
pluma.write(r'    Ana Cecilia Espinosa García & Gustavo Perez Ortíz\\     \hline' + '\n')
pluma.write(r'    \end{tabular} ' + '\n')
pluma.write(r'    {\color{Gray}' + '\n')
pluma.write(r'    \begin{tabular}{ p{7cm} p{1cm} p{7cm} p{1cm} }' + '\n')
pluma.write(r'    Responsable & Firma & Colector & Firma ' + '\n')
pluma.write(r'    \end{tabular}\vspace{1.1cm}' + '\n')
pluma.write(r'    }' + '\n')
     
# pluma.write(r'    \vspace{1cm}' + '\n')
     
     
pluma.write(r'    \begin{tabular}{|>{\centering\arraybackslash}p{1.5cm}|>{\centering\arraybackslash}p{1.7cm}|>{\centering\arraybackslash}p{0.1cm}|>{\centering\arraybackslash}p{0.1cm}|>{\centering\arraybackslash}p{0.1cm}|>{\centering\arraybackslash}p{0.1cm}|>{\centering\arraybackslash}p{1.4cm}|>{\centering\arraybackslash}p{0.6cm}|>{\centering\arraybackslash}p{0.6cm}|>{\centering\arraybackslash}p{2cm}|>{\centering\arraybackslash}p{3cm}|}' + '\n')
 
pluma.write(r'    \hline' + '\n')
pluma.write(r'    Hora & Código & \multicolumn{4}{c|}{Tipo de muestra} & Cantidad (g o mL) &  \multicolumn{2}{c|}{Preservación} & Análisis Solicitado & Observaciones \\' + '\n')
  
pluma.write(r'    \hline' + '\n')  
pluma.write(r'    8:00 &   & C & L & V & A &   & Si & No &   &   \\' + '\n') 
pluma.write(r'    \hline ' + '\n')
pluma.write(r'    8:30 &   & C & L & V & A &   & Si & No &   &   \\' + '\n') 
pluma.write(r'    \hline ' + '\n')
pluma.write(r'    9:00 &   & C & L & V & A &   & Si & No &   &   \\' + '\n') 
pluma.write(r'    \hline ' + '\n')
pluma.write(r'    9:30 &   & C & L & V & A &   & Si & No &   &   \\' + '\n') 
pluma.write(r'    \hline ' + '\n')
pluma.write(r'    10:00 &   & C & L & V & A &   & Si & No &   &   \\' + '\n') 
pluma.write(r'    \hline ' + '\n')
pluma.write(r'    10:30 &   & C & L & V & A &   & Si & No &   &   \\' + '\n') 
pluma.write(r'    \hline ' + '\n')
pluma.write(r'    11:00 &   & C & L & V & A &   & Si & No &   &   \\' + '\n')  
pluma.write(r'    \hline ' + '\n')
pluma.write(r'    11:30 &   & C & L & V & A &   & Si & No &   &   \\' + '\n') 
pluma.write(r'    \hline ' + '\n')
pluma.write(r'    12:00 &   & C & L & V & A &   & Si & No &   &   \\' + '\n') 
pluma.write(r'    \hline ' + '\n')
pluma.write(r'    12:30 &   & C & L & V & A &   & Si & No &   &   \\' + '\n')  
pluma.write(r'    \hline ' + '\n')
pluma.write(r'    13:00 &   & C & L & V & A &   & Si & No &   &   \\' + '\n')  
pluma.write(r'    \hline' + '\n') 
pluma.write(r'    13:30 &   & C & L & V & A &   & Si & No &   &   \\' + '\n') 
pluma.write(r'    \hline ' + '\n')
pluma.write(r'    14:00 &   & C & L & V & A &   & Si & No &   &   \\' + '\n') 
pluma.write(r'    \hline ' + '\n')
pluma.write(r'    14:30 &   & C & L & V & A &   & Si & No &   &   \\' + '\n') 
pluma.write(r'    \hline ' + '\n')
pluma.write(r'    15:00 &   & C & L & V & A &   & Si & No &   &   \\' + '\n')  
pluma.write(r'    \hline ' + '\n')
pluma.write(r'    15:30 &   & C & L & V & A &   & Si & No &   &   \\' + '\n') 
pluma.write(r'    \hline ' + '\n')
pluma.write(r'    16:00 &   & C & L & V & A &   & Si & No &   &   \\' + '\n')  
pluma.write(r'    \hline' + '\n') 
pluma.write(r'    16:30 &   & C & L & V & A &   & Si & No &   &   \\' + '\n')  
pluma.write(r'    \hline ' + '\n')
pluma.write(r'    17:00 &   & C & L & V & A &   & Si & No &   &   \\' + '\n') 
pluma.write(r'    \hline ' + '\n')
pluma.write(r'    17:30 &   & C & L & V & A &   & Si & No &   &   \\' + '\n') 
pluma.write(r'    \hline ' + '\n')
pluma.write(r'    18:00 &   & C & L & V & A &   & Si & No &   &   \\' + '\n') 
pluma.write(r'    \hline ' + '\n')
pluma.write(r'    \end{tabular}\vspace{0.2cm}' + '\n') 
# pluma.write(r'    \vspace{5mm}' + '\n')
     
pluma.write(r'    C=Carne; L=Leche; V=Verdura; A=Agua;          \\\vspace{0.576cm}' + '\n')
 
pluma.write(r'Continúa en el anverso de esta hoja Registro de Cadena Custodia\vspace{0.2cm}' + '\n')
 
     
pluma.write(r'    \vspace{9.5mm}' + '\n')
pluma.write(r'    \includegraphics[scale=0.78]{abajo1.png}' + '\n')
     
     
pluma.write(r'    \includegraphics{encabezado.png}' + '\n')
     
pluma.write(r'    \begin{tabular}{|p{0.1cm}|p{2.7cm}|p{1.4cm}|p{1.4cm}|p{1cm}|p{0.1cm}|p{2.7cm}|p{1.4cm}|p{1.4cm}|p{1cm}|}' + '\n')
pluma.write(r'        \hline ' + '\n')
pluma.write(r'        \multicolumn{7}{|c|}{\textbf{Registro de cadena de custodia}} & \multicolumn{3}{c|}{{\color{red}LANCIS-PCR-FCC-I0001/2015}} \\' + '\n') 
pluma.write(r'        \hline ' + '\n')
pluma.write(r'        \multicolumn{5}{|c|}{Entrega} & \multicolumn{5}{c|}{Recepción}\\' + '\n') 
pluma.write(r'        \hline ' + '\n')
         
pluma.write(r'         \multicolumn{10}{|c|}{\cellcolor{gainsboro}\textbf{Colecta en campo} } \\' + '\n')
         
pluma.write(r'        \hline ' + '\n')
pluma.write(r'        1 & Nombre: & Firma: & Fecha: & Hora: & 1 & Nombre: & Firma: & Fecha: & Hora: \\[2.6ex]' + '\n') 
pluma.write(r'        \hline ' + '\n')
pluma.write(r'         & \multicolumn{4}{l|}{Observaciones:} &  & \multicolumn{4}{l|}{Observaciones:}  \\[2.6ex]' + '\n') 
pluma.write(r'        \hline ' + '\n')
pluma.write(r'        \multicolumn{10}{|c|}{\cellcolor{gainsboro}\textbf{Transporte 1} } \\' + '\n')
pluma.write(r'        \hline ' + '\n')
pluma.write(r'        2 & Nombre: & Firma: & Fecha: & Hora: & 2 & Nombre: & Firma: & Fecha: & Hora: \\[2.6ex]' + '\n') 
pluma.write(r'        \hline ' + '\n')
pluma.write(r'        & \multicolumn{4}{l|}{Observaciones:} &  & \multicolumn{4}{l|}{Observaciones:}  \\[2.6ex]' + '\n') 
pluma.write(r'        \hline ' + '\n')
pluma.write(r'        \multicolumn{10}{|c|}{\cellcolor{gainsboro}\textbf{Transporte 2} } \\' + '\n')
pluma.write(r'        \hline ' + '\n')
pluma.write(r'        3 & Nombre: & Firma: & Fecha: & Hora: & 3 & Nombre: & Firma: & Fecha: & Hora: \\[2.6ex]' + '\n')  
pluma.write(r'        \hline ' + '\n')
pluma.write(r'        & \multicolumn{4}{l|}{Observaciones:} &  & \multicolumn{4}{l|}{Observaciones:}  \\[2.6ex]' + '\n') 
pluma.write(r'        \hline ' + '\n')
pluma.write(r'        \multicolumn{10}{|c|}{\cellcolor{gainsboro}\textbf{Entrega de muestras a laboratorio}} \\' + '\n')
pluma.write(r'        \hline ' + '\n')
pluma.write(r'        4 & Nombre: & Firma: & Fecha: & Hora: & 4 & Nombre: & Firma: & Fecha: & Hora: \\[2.6ex]' + '\n') 
pluma.write(r'        \hline ' + '\n')
pluma.write(r'        & \multicolumn{4}{l|}{Observaciones:} &  & \multicolumn{4}{l|}{Observaciones:}  \\[2.6ex]' + '\n') 
pluma.write(r'        \hline ' + '\n')
pluma.write(r'        \multicolumn{10}{|c|}{\cellcolor{gainsboro}\textbf{Entrega de resultados de laboratorio} } \\' + '\n')
pluma.write(r'        \hline ' + '\n')
pluma.write(r'        5 & Nombre: & Firma: & Fecha: & Hora: & 5 & Nombre: & Firma: & Fecha: & Hora: \\[2.6ex]' + '\n') 
pluma.write(r'        \hline ' + '\n')
pluma.write(r'        & \multicolumn{4}{l|}{Observaciones:} &  & \multicolumn{4}{l|}{Observaciones:}  \\[2.6ex]' + '\n') 
pluma.write(r'        \hline ' + '\n')
pluma.write(r'        \multicolumn{10}{|c|}{\cellcolor{gainsboro}\textbf{Entrega de resultados, Análisis de datos} } \\' + '\n')
pluma.write(r'        \hline ' + '\n')
pluma.write(r'        6 & Nombre: & Firma: & Fecha: & Hora: & 6 & Nombre: & Firma: & Fecha: & Hora: \\[2.6ex]' + '\n') 
pluma.write(r'        \hline ' + '\n')
pluma.write(r'        & \multicolumn{4}{l|}{Observaciones:} &  & \multicolumn{4}{l|}{Observaciones:}  \\[2.6ex]' + '\n') 
pluma.write(r'        \hline ' + '\n')
pluma.write(r'        \multicolumn{10}{|c|}{\cellcolor{gainsboro}\textbf{Integración} } \\' + '\n')
pluma.write(r'        \hline ' + '\n')
pluma.write(r'        7 & Nombre: & Firma: & Fecha: & Hora: & 7 & Nombre: & Firma: & Fecha: & Hora: \\[2.6ex]' + '\n') 
pluma.write(r'        \hline ' + '\n')
pluma.write(r'        & \multicolumn{4}{l|}{Observaciones:} &  & \multicolumn{4}{l|}{Observaciones:}  \\[2.6ex]' + '\n') 
pluma.write(r'        \hline ' + '\n')
pluma.write(r'        & \multicolumn{4}{c|}{} &  & \multicolumn{4}{c|}{}  \\[5ex]' + '\n') 
pluma.write(r'        \hline' + '\n')
         
pluma.write(r'        \end{tabular}' + '\n')     
     
pluma.write(r'    \includegraphics[scale=0.78]{abajo1.png}' + '\n')
     
pluma.write(r'    \end{center}' + '\n')
pluma.write(r'\end{document}' + '\n')
 
 
pluma.close()
 
 
 
 
 
 
 
 
 
 
p = subprocess.call(["/usr/texbin/pdflatex", "pytesttex.tex"])
