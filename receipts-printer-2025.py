"""
2025 by PM
Based on a web tutorial
----------------------------------------------
"""
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet


DATA = [
    [ "Header 1" , "Header 2", "Header 3", "Header 4" ],
    [ "Data 1 1", "Data 1 2", "Data 1 3", "Data 1 4"],
    [ "Data 2 1", "Data 2 2", "Data 2 3", "Data 2 4"],
    [ "Total", "", "", "Data total"],
    [ "Total 2", "", "", "Data total 2"]
]

def main():
    #Main function
    #Setting basic .pdf
    pdf = SimpleDocTemplate( "test.pdf" , pagesize = A4 )
    
    #Setting standard stylesheet
    styles = getSampleStyleSheet()
    #Setting the title style (Heading1)
    head_style = styles[ "Heading1" ]
    #0: left, 1: center, 2: right
    head_style.alignment = 1 
    #Creating the actual heading 
    head = Paragraph( "Main Heading" , head_style )
    
    #Defining precise styles of a table
    style = TableStyle(
    [
        ( "BOX" , ( 0, 0 ), ( -1, -1 ), 1 , colors.black ),
        ( "GRID" , ( 0, 0 ), ( 4, 2 ), 1 , colors.black ),
        ( "BOX" , ( 0, 4 ), ( -1, 4 ), 1, colors.black),
        ( "BACKGROUND" , ( 0, 0 ), ( 3, 0 ), colors.black ),
        ( "TEXTCOLOR" , ( 0, 0 ), ( -1, 0 ), colors.whitesmoke ),
        ( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ),
        ( "BACKGROUND" , ( 0 , 1 ) , ( -1 , -1 ), colors.gray ),
    ]
    )
    #Creating a table object with style
    table = Table( DATA , style = style )

    #Building an actual pdf
    pdf.build([ head , table ])
    

if __name__ == '__main__':
    main()