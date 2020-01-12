"Utility to create the csv file with the list of CC issuers."

import csv

cc_issuers = [
              [340000, 379999, "American Express"],
              [510000, 559999, "Mastercard"],
              [560000, 599999, "Maestro"],
              [400000, 499999, "Visa"]
              ]

with open("./cc_issuers.csv", "w") as f:
    w = csv.writer(f)
    w.writerow(["from", "to", "issuer"])
    for x in cc_issuers:
        w.writerow(x)
