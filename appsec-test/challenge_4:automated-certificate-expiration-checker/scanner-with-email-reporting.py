#!/usr/bin/python3.5
# -*- coding: iso-8859-1 -*-

#Written by Ryan McDonald 06/31/2016

import nmap
import logging
import datetime
import htmlFormatting

# initialize the log settings
logging.basicConfig(filename = 'sslmon.log', level = logging.DEBUG)

#----------------------------------------------------------------------
# SSL monitor
#----------------------------------------------------------------------
SSLmonitor = nmap.PortScanner()

ssl_discovery_scan = "ssl_discovery.log"

with open(ssl_discovery_scan, "w") as ssl_scan:
    ssl_scan.write("")

with open("ssl_discovery_results", "w") as f2:
    f2.write("")
    
expiration_report = "SSL-Certificate-Report-" + str(datetime.date.today())[0:10] + ".html"
with open(expiration_report, "a") as report:
  report.write(htmlFormatting.Table)
  
def SSLmon(IPaddress):
    try:
        results = SSLmonitor.scan(hosts=IPaddress, arguments='--script=ssl-cert -p 443')
        hosts = results['scan']

        logging.info("Scanned " + IPaddress + " on " + str(datetime.datetime.now()))

        try:
            for host in hosts:
                print(IPaddress)
                certificate = hosts[host]["tcp"][443]['script']['ssl-cert']
                try:
                    hostname = hosts[host]['hostnames'][0]["name"].replace("origin", "")

                except Exception:
                    hostname = IPaddress

                # pprint(results)
                # format for dictionary grouping
                certificate = certificate.replace("=", ":").replace(": ", "=").replace("/", ", ")

                # group into dictionaries
                certificate = dict(item.split("=") for item in certificate.split("\n"))

                # Get common name
                subject = certificate['Subject'].split(",")
                commonName = str(subject[0]).split(":")
                commonName = commonName[1]

                # Get issuer
                issuer = certificate['Issuer'].split(",")
                issuer = str(issuer[0]).split(":")
                issuer = issuer[1]

                # Public Key Type
                pub_key = certificate['Public Key type']

                # Public Key bits
                pub_key_bits = certificate['Public Key bits']

                # Signature Algorithm
                sig_alg = certificate['Signature Algorithm']

                # Not valid before
                creation = certificate['Not valid before']
                creation = creation[0:10]

                expiration_date_object = datetime.datetime.strptime(certificate['Not valid after'][1:11].replace("-","/"), '%Y/%m/%d')
                expiration_days = expiration_date_object - datetime.datetime.today()
                expiration_days = str(expiration_days).split(',')
                expiration_days = expiration_days[0]
                year_until = datetime.datetime.today() + datetime.timedelta(days=365)
                sixty_days_until = datetime.datetime.today() + datetime.timedelta(days=60)
                thirty_days_until = datetime.datetime.today() + datetime.timedelta(days=30)
                expired = datetime.datetime.today()
                expiration_report = "SSL-Certificate-Report-" + str(expired)[0:10] + ".html"

                with open(ssl_discovery_scan, "a") as file:
                    cert_log = hostname.strip(",").strip("\n") + "," + commonName.strip(",") + "," + issuer.strip(",") + "," + pub_key + "," + pub_key_bits + "," + creation.strip(",") + "," + str(expiration_date_object)[0:10] + "," + str(expiration_days).strip(" days"+"\n")
                    file.write(cert_log)

            # less than 365 more than 60
            if expiration_date_object < year_until and expiration_date_object > sixty_days_until:
                row = htmlFormatting.HostnameOpener + hostname \
                      + htmlFormatting.Closer + htmlFormatting.GenericOpener + commonName \
                      + htmlFormatting.GenericCloser + htmlFormatting.GenericOpener + issuer \
                      + htmlFormatting.GenericCloser + htmlFormatting.GenericOpener + pub_key \
                      + htmlFormatting.GenericCloser + htmlFormatting.GenericOpener + pub_key_bits \
                      + htmlFormatting.GenericCloser + htmlFormatting.GenericOpener + sig_alg \
                      + htmlFormatting.GenericCloser + htmlFormatting.GenericOpener + creation \
                      + htmlFormatting.GenericCloser + htmlFormatting.GenericOpener + str(expiration_date_object)[0:10] \
                      + htmlFormatting.GenericCloser + htmlFormatting.GenericOpener + str(expiration_days) + htmlFormatting.ExpirationCloser
                with open(expiration_report, "a") as report:
                    report.write(row)

            # less than 60 more than 30
            if expiration_date_object < sixty_days_until and expiration_date_object > thirty_days_until:
                row = htmlFormatting.HostnameOpener + hostname \
                      + htmlFormatting.Closer + htmlFormatting.GenericOpener + commonName \
                      + htmlFormatting.GenericCloser + htmlFormatting.GenericOpener + issuer \
                      + htmlFormatting.GenericCloser + htmlFormatting.GenericOpener + pub_key \
                      + htmlFormatting.GenericCloser + htmlFormatting.GenericOpener + pub_key_bits \
                      + htmlFormatting.GenericCloser + htmlFormatting.GenericOpener + sig_alg \
                      + htmlFormatting.GenericCloser + htmlFormatting.GenericOpener + creation \
                      + htmlFormatting.GenericCloser + htmlFormatting.GenericOpener + str(expiration_date_object)[0:10] \
                      + htmlFormatting.ExpirationGreen + str(expiration_days) + htmlFormatting.ExpirationCloser
                with open(expiration_report, "a") as report:
                    report.write(row)

            # less than 30 but not expired
            if expiration_date_object < thirty_days_until and expiration_date_object > expired:
                row = htmlFormatting.HostnameOpener + hostname \
                      + htmlFormatting.Closer + htmlFormatting.GenericOpener + commonName \
                      + htmlFormatting.GenericCloser + htmlFormatting.GenericOpener + issuer \
                      + htmlFormatting.GenericCloser + htmlFormatting.GenericOpener + pub_key \
                      + htmlFormatting.GenericCloser + htmlFormatting.GenericOpener + pub_key_bits \
                      + htmlFormatting.GenericCloser + htmlFormatting.GenericOpener + sig_alg \
                      + htmlFormatting.GenericCloser + htmlFormatting.GenericOpener + creation \
                      + htmlFormatting.GenericCloser + htmlFormatting.GenericOpener + str(expiration_date_object)[0:10] \
                      + htmlFormatting.ExpirationOrange + str(expiration_days) + htmlFormatting.ExpirationCloser
                with open(expiration_report, "a") as report:
                    report.write(row)


            # Expired certs
            if expiration_date_object < expired:
                row = htmlFormatting.HostnameOpener + hostname \
                      + htmlFormatting.Closer + htmlFormatting.GenericOpener + commonName \
                      + htmlFormatting.GenericCloser + htmlFormatting.GenericOpener + issuer \
                      + htmlFormatting.GenericCloser + htmlFormatting.GenericOpener + pub_key \
                      + htmlFormatting.GenericCloser + htmlFormatting.GenericOpener + pub_key_bits \
                      + htmlFormatting.GenericCloser + htmlFormatting.GenericOpener + sig_alg \
                      + htmlFormatting.GenericCloser + htmlFormatting.GenericOpener + creation \
                      + htmlFormatting.GenericCloser + htmlFormatting.GenericOpener + str(expiration_date_object)[0:10] \
                      + htmlFormatting.ExpirationRed + str(expiration_days) + htmlFormatting.ExpirationCloser
                with open(expiration_report, "a") as report:
                    report.write(row)

        except Exception as e:
            logging.exception(str(e))
            pass

    except Exception as e:
        logging.exception(str(e))


with open("Overstock_address_space", "r") as host_file:
    for host in host_file:
        logging.info("Scan started on " + str(datetime.datetime.now()))
        SSLmon(host)
        logging.info("Scan completed on " + str(datetime.datetime.now()))

with open("ssl_discovery.log", 'r') as f:
    lines = set(f.readlines())
    with open("ssl_discovery_results", "a") as f2:
        for i in lines:
            print(i)
            f2.write(i)
            
with open(expiration_report, "a") as report:
  report.write(htmlFormatting.finish)