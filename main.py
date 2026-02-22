import streamlit as st
import pandas as pd
from datetime import date

    
tab1, tab2, tab3 = st.tabs(["Invoice", "Receipt", "Records"])
   
with tab1:
    name = st.text_input('Enter Insured')  
    kra_pin = st.text_input('Enter KRA Pin')            
    reg = st.text_input('Enter Registration')
    underwriter = st.selectbox("Choose Underwriter", ["APA INSURANCE", "FIDELITY INSURANCE", "CANNON GENERAL INSURANCE", "GA INSURANCE", "ICEA LION INSURANCE"])
    gross = int(st.number_input('Gross Premium')) 

    if st.button("Get Invoice"):    

        levies = gross * 0.0045

        total = ( gross + levies + 100 )

        date = date.today()

        # Format numbers with commas for thousands
        def format_with_commas(number):
            rounded_number = round(number, 2)
            return "{:,.2f}".format(rounded_number)                
            
                        
        formatted_gross = format_with_commas(gross)
        formatted_levies = format_with_commas(levies)
        formatted_total = format_with_commas(total)

            

        # Create an HTML report
        html_report = f"""
            <html>
            <head>
            <style>
                table {{
                border-collapse: collapse;
                width: 99%;
                margin: 0.5px auto;
                font-size: 12px;
                font-family: Candara;
            }}

            th, td {{
                border: 1px solid black;
                padding: 5px; 
                text-align: left;
            }}

            th {{
                background-color: white;
                color: black; /* Text color for table headers */
            }}

            .bold {{
                font-weight: bold;
            }}

            .gross_premium {{
                border-top: 2px solid black;
                border-bottom: 2px double black;        
            }}

            img {{
                max-width: 200px;
                height: auto;
                display: block;
                margin: 0 auto;
            }}    
        
            .footer-row th {{
                background-color: #073980; 
            }}                

            .card {{font-family: Candara; border: 1.5px solid; width:75%; margin:0 auto; font-size:16px; padding: 2.5px;}}         
            
            </style>
            </head>
            <body style="margin-top:5%">

             
                        

            <div class="card">

            <br>

            <br>

            <br>

            <br>

                    

            <table>
                <tr>

                <img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAsJCQcJCQcJCQkJCwkJCQkJCQsJCwsMCwsLDA0QDBEODQ4MEhkSJRodJR0ZHxwpKRYlNzU2GioyPi0pMBk7IRP/2wBDAQcICAsJCxULCxUsHRkdLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCz/wAARCAEOAQsDASIAAhEBAxEB/8QAGwABAAMBAQEBAAAAAAAAAAAAAAQFBgMHAgH/xAA/EAABBAIBAgUCAwUFBQkAAAABAAIDBAUREgYhEzFBUWEUIjJxgRUjQpGhByRSYrEzY4KS0RY2Q1NyhKKy8f/EABoBAQEBAQEBAQAAAAAAAAAAAAABAwIEBQb/xAAuEQEBAAIBAwIDBwQDAAAAAAAAAQIRAxIhMQQTBUFRFCJhcYGh8CMyQtHB4fH/2gAMAwEAAhEDEQA/APW0REBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQERR7lypQry2rUrY4Y/Nx8yT5NaB3JPoAiWzGbqQiz+J6ox+WuvpxQ2In+G+SJ03DUgYRsaYTo+vmtApLMpuM+Lmw5serju4IiKtRERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQFQdTZHpqrRfUzVrwm3GkRMia+SwSwgiSNjGk/adHZGvT10b5eB9XX5Mh1Fm5nP5MhsvpQd9tbFWJiAb8Ehzv+L5WvFxzkur4Z8mrjZZvbadLYqSxlauRpWoZ8ZVkmeLcLu8ruJjELonaka/vtwc0a+dgn0leA9O9S5Lpua1JUjgmitiIWIbHMNJjJ4vYWEad3I3o/l27biv8A2p0HcRaw9uP/ABGvPDMPzAkDCn2W8fbDvHm9Lw8fpsbjh8+70ZFk6fXvTt6LIzRQ5FooRQTTNlgiBc2aXwWlhbIR2PnshXGIzNfMxTTQVrcMcbwwOsxt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" alt="Description" style="display:block; margin:auto; width:120px; height:auto;">
            

                </tr>


                <tr>
                    
                        <th colspan="2">
                            Insured: {name}<br>
                            KRA PIN: {kra_pin} <br>
                            INVOICE NO:GSK/{reg}/{date}<br>
                            Risk Carrier: {underwriter}<br>
                            Risk Type: MOTOR PRIVATE<br>
                            Vehicle Registration: {reg}
                        </th>
                        
                </tr>
               
              
                <tr>
                    <td>Gross Premium</td>
                    
                    <td>{formatted_gross}</td> <!-- Updated formatting for better readability -->
                </tr>
                <tr>
                    <td>Levies</td>
                    
                    <td>{formatted_levies}</td>
                </tr>
                <tr>
                    <td>Policy Fee</td>
                    
                    <td>100.00</td>
                </tr>
                <tr>
                    <td>Total Premium</td>
                    
                    <td><b>{formatted_total}</b></td>
                </tr>

                <tr>
                    <td colspan="2" style="font-size: 10px"> Outcrest Consultancy Limited and on behalf of Gras Savoye Kenya Insurance Brokers Limited</td>
                </tr>

                <tr>               

                    <td colspan="2">
                        <br>
                        <u><b>MPESA Payment Details</b><br></u>
                        PayBill Number: 880100<br>
                        Account Number: PAYMOTOR<br>

                        <br>
                        <br>

                        Prepared by: COLLINS CHETEKEI <br>
                        Date: {date} 
                    </td>   

                             

                </tr>
            </table>

            
            <p style="font-size: 12px"> &nbsp; Thank you for choosing <b>Gras Savoye Kenya</b> as your trusted insurance broker.</p>
            
                    
            </body>               
            
                
            </html>
            """
            
        # Create a download button with customized file name

        st.download_button(
                label=f"Download {reg}'s_premium_quote(HTML)",
                data=html_report.encode('utf-8'),
                file_name=f"{reg}_DebitNote.html",
                mime="text/html"
            )


