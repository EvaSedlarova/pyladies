barvy_ovoce = {
    'hruška': 'zelená',
    'jablko': 'červená',
    'meloun': 'zelená',
    'švestka': 'modrá',
    'ředkvička': 'červená',
    'zelí': 'zelená',
    'mrkev': 'červená',
}

barvy_ovoce_po_tydnu = dict(barvy_ovoce)

for klic in barvy_ovoce_po_tydnu:
    barvy_ovoce_po_tydnu[klic] = "plesnivo-" + barvy_ovoce_po_tydnu[klic]

print(barvy_ovoce_po_tydnu)