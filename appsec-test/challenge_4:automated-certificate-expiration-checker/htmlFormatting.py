
Table = """<h1>Weekly SSL Certificate Expiration Report</h1>
</br>
<p>Teams,</p>
</br>
<p>Below is the SSL Certifcate expiration report, please review this report and work with your team to determine if anything in the report warrants follow on action.</p>
</br>
<p>Please reach out to <Administrator> with any questions about this report.</p>
<table class='MsoNormalTable' border='0' cellspacing='0' cellpadding='0' width='1400' style='width:1200.0pt;border-collapse:collapse'>
<tbody>
<tr style='height:39.0pt'>
    <td width='220' style='width:220.0pt;border:solid windowtext 1.0pt;background:red;padding:0in 5.4pt 0in 5.4pt;height:39.0pt'>
        <span style='font-size:14.0pt;color:white'>
            <p class='MsoNormal' align='center' style='text-align:center'><b>Hostname</b></p>
        </span>
    </td>
    <td width='328' style='width:80.0pt;border:solid windowtext 1.0pt;border-left:none;background:red;padding:0in 5.4pt 0in 5.4pt;height:39.0pt'>
        <span style='font-size:14.0pt;color:white'>
            <p class='MsoNormal' align='center' style='text-align:center'><b>Common</b></p>
        </span>
    </td>
    <td width='200' style='width:180.0pt;border:solid windowtext 1.0pt;border-left:none;background:red;padding:0in 5.4pt 0in 5.4pt;height:39.0pt'>
        <span style='font-size:14.0pt;color:white'>
            <p class='MsoNormal' align='center' style='text-align:center'><b>Issuer</b></p>
        </span>
    </td>
    <td width='450' style='width:96.0pt;border:solid windowtext 1.0pt;border-left:none;background:red;padding:0in 5.4pt 0in 5.4pt;height:39.0pt'>
        <span style='font-size:14.0pt;color:white'>
            <p class='MsoNormal' align='center' style='text-align:center'><b>Pub Key</b></p>
        </span>
    </td>
    <td width='328' style='width:56.9pt;border:solid windowtext 1.0pt;border-left:none;background:red;padding:0in 5.4pt 0in 5.4pt;height:39.0pt'>
        <span style='font-size:14.0pt;color:white'>
            <p class='MsoNormal' align='center' style='text-align:center'><b>Pub Key Bits</b></p>
        </span>
    </td>
    <td width='328' style='width:56.9pt;border:solid windowtext 1.0pt;border-left:none;background:red;padding:0in 5.4pt 0in 5.4pt;height:39.0pt'>
        <span style='font-size:14.0pt;color:white'>
            <p class='MsoNormal' align='center' style='text-align:center'><b>Sig Alg</b></p>
        </span>
    </td>
    <td width='328' style='width:56.9pt;border:solid windowtext 1.0pt;border-left:none;background:red;padding:0in 5.4pt 0in 5.4pt;height:39.0pt'>
        <span style='font-size:14.0pt;color:white'>
            <p class='MsoNormal' align='center' style='text-align:center'><b>Created</b></p>
        </span>
    </td>
    <td width='328' style='width:56.9pt;border:solid windowtext 1.0pt;border-left:none;background:red;padding:0in 5.4pt 0in 5.4pt;height:39.0pt'>
        <span style='font-size:14.0pt;color:white'>
            <p class='MsoNormal' align='center' style='text-align:center'><b>Expiration Date</b></p>
        </span>
    </td>
    <td width='328' style='width:56.9pt;border:solid windowtext 1.0pt;border-left:none;background:red;padding:0in 5.4pt 0in 5.4pt;height:39.0pt'>
        <span style='font-size:14.0pt;color:white'>
            <p class='MsoNormal' align='center' style='text-align:center'><b>Days Left</b></p>
        </span>
    </td>
</tr>"""


GenericOpener = """<td width='128' valign='bottom' style='width:96.0pt;padding:0in 5.4pt 0in 5.4pt;height:17.0pt'>    <span style='font-size:10.0pt;color:black'>        <p class='MsoNormal'>"""
HostnameOpener = """<td width='328' valign='bottom' style='width:96.0pt;padding:0in 5.4pt 0in 5.4pt;height:17.0pt'>    <span style='font-size:10.0pt;color:black'>        <p class='MsoNormal'><b>"""
Closer = """</b></p>    </span>        </td>    """
GenericCloser = """</p>    </span>        </td>    """
ExpirationGreen = """   <td width='95' valign='bottom' style='width:71.0pt;padding:0in 5.4pt 0in 5.4pt;height:17.0pt'>    <span style='font-size:10.0pt;color:#00B050'>        <p class='MsoNormal' align='center' style='text-align:center'><b>"""
ExpirationOrange = """  <td width='95' valign='bottom' style='width:71.0pt;padding:0in 5.4pt 0in 5.4pt;height:17.0pt'>    <span style='font-size:10.0pt;color:#b09b00'>        <p class='MsoNormal' align='center' style='text-align:center'><b>"""
ExpirationRed = """ <td width='95' valign='bottom' style='width:71.0pt;padding:0in 5.4pt 0in 5.4pt;height:17.0pt'>    <span style='font-size:10.0pt;color:#b0000f'>        <p class='MsoNormal' align='center' style='text-align:center'><b>"""
ExpirationCloser = """</b></p>        </span>    </td></tr>"""
finish = "</tr></tbody></table>"
