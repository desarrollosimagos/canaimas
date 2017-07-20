# -*- coding: utf-8 -*-
from fpdf import FPDF
import os
import fpdf
import time

class ReporteCandidato(FPDF):

	def header(self):
		#Arial bold 15
		self.set_font('Arial','B',15)
		
		# ALINEACION DE LA IMAGEN EN LA CABECERA DEL DOCUMENTO
		# (CAMPO 1 = HORIZONTAL , CAMPO 2 = VERTICAL, CAMPO 3 = DIMENCION DE LA IMAGEN)
		os.path.dirname(os.path.abspath(__file__))
		DIR_URL = os.getcwd()
		self.image(DIR_URL+str('/static/img/tope.jpg'),19,15,180)
		#Calcular ancho del texto (title) y establecer posición
		#w=self.get_string_width(title)+6
		#self.set_x((210-w)/2)
		#Colores del marco, fondo y texto
		self.set_draw_color(0,80,180)
		self.set_fill_color(28,108,198)
		self.set_text_color(220,50,50)
		#Grosor del marco (1 mm)
		#self.set_line_width(1)
		#Titulo
		#self.cell(w,9,title,1,1,'C',1)
		#Salto de línea
		self.ln(25)
	
		
	#METODO PARA CONSTRUIR LA PAGINACION
	# Page footer
	def footer(self):
		#Posición a 1.5 cm desde abajo
		self.set_y(-20)
		#Arial italic 8
		self.set_font('Arial','I',8)
		#Color de texto en gris
		self.set_text_color(128)
		#Numero de pagina
		fecha_hora = time.strftime("%d/%m/%Y")+" "+time.strftime("%I:%M %p")
		self.cell(37,5,fecha_hora,0,0,'R')
		self.cell(144,5,'www.exit_poll.org.ve',0,0,'R')  
		self.cell(0.25,10,'Pagina '+str(self.page_no()),0,0,'R') 
		
	def chapter_title(self,num,label):
		#Arial 12
		self.set_font('Arial','',12)
		#Color de fondo
		self.set_fill_color(200,220,255)
		#Titulo
		self.cell(0,6,"Chapter %d : %s"%(num,label),0,1,'L',1)
		#Salto de línea
		self.ln(4)
		
	def chapter_body(self,name):
		#Leer archivo de texto
		txt=file(name).read()
		#Times 12
		self.set_font('Arial','',15)
		#Emitir texto justificado
		self.multi_cell(0,5,txt)
		pdf.set_fill_color(157,188,201) # COLOR DE BOLDE DE LA CELDA
		pdf.set_text_color(24,29,31) # COLOR DEL TEXTO
		
		#Salto de línea
		self.ln()
		#Mención en italic -cursiva-
		self.set_font('','I')
		self.cell(0,5,'(end of excerpt)')
		
	# CONSTRUCCTOR DEL DOCUMENTO
	def print_chapter(self,num,title,name):
		self.add_page()
		self.chapter_title(num,title)
		self.chapter_body(name)
