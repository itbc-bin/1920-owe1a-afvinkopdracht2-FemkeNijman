
sequentie = ("AGCCGCCCTTTCCTCTTTCTTTCGCGCTCTAGCCACCCGGGAAGGCCTGCCCAGCGTAGCTGGGCTCTGATTGGCTGCTTTGAAAGTCTACGGGCTACCCGATTGGTGAATCCGGGGCCCTTTAGCGCGGATCTACCATACCCATTGACTAACTATGGAAGATTATACCAAAATAGAGAAAATTGGAGAAGGTACCTATGGAGTTGTGTATAAGGGTAGACACAAAACTACAGGTCAAGTGGTAGCCATGAAAAAAATCAGACTAGAAAGTGAAGAGGAAGGGGTTCCTAGTACTGCAATTCGGGAAATTTCTCTATTAAAGGAACTTCGTCATCCAAATATAGTCAGTCTTCAGGATGTGCTTATGCAGGATTCCAGGTTATATCTCATCTTTGAGTTTCTTTCCATGGATCTGAAGAAATACTTGGATTCTATCCCTCCTGGTCAGTACATGGATTCTTCACTTGTTAAGGTAAAAGCTTAACTAATTTTATTAATATTTATGCACTGTGGATATAAAGGGACTATATATAGAAGTCCCTGCATTTTGTGGGAATATGCTTGGAAAAAGTGTTAGAATAAGAAAAAGTATTTCATTTTTCTCCCTCATGGTTAGTTTATACAGGTTAGAGATACCCATGTTATTACCAGATAGTGTTTCTAGTAAGTAAAAATTAGTGCCTGAGATAACATAGAACTGGTAGGTATTGTTGGAAGCTAGGGTAGTCTGGTCTTTCTTTGGCTGTCAGATACATGTAAAACAAAGTAATGAAAGCCTAGGGCAGAGTGGTGGTTGTAGGTGTTTTATTCCAGTTTTGAACATGTTTTGGTCAATTTATTGTAGACATTTATTATATTTCAGGTAAATTATAAAATTGTATAGTTTTAAGTACTGAAGTATATAAAAGTGTCTTATTCTTGCACCAGTTCTACCAAACCACTCTGCAGAGGTAGCGCTGTTAGTTTTATTTGTAATCTTACACTTGTATGTATGTTCACTTTGTATGTATATAAAGATTTTTTTTTTTACACAAGGTGGACTTATTTGCATATGTATATATACATATTTTCCCTTTTTTGTGTAAAACATTATCAAGACGTAGATCTACCTATGTCTATTTACATTTTTGATATAATTAAACCACTTCCATATTGATGAACATTTAAATTATTTTCCAACTTGGTTATTGTTGCTCTTATTAACAGTACTGCACTGAATGTCCTTATAGATATTTATCTTCGTATGCAACTTTATAGGATAAATTTTTAGAATGGGAATGATGGATTGAAGATGTTTATTTACATTTTGATAGATATTGCCGGTTGCCCCCTAAAAAACTTGTAGCAATTTACTCTTAAATACTCATGGTGTGTAATACTTATTGTTTTAGTACATCATTGCCAAAACTTGGTTTTATCAATCTGTTAACTATGTGAAAAAGGCATATTAAGATTGTTTTAATTTTATATTTCATGACAATTTAACACTTCATATTTAGCTATTATAAACCGCCTATATTTTCGTTAGGATACGTTCTTTAACAATCTTGCATGACTTTTGGACTTTCTGCTTTTATGTCTTGCTTAAGTCTTCCTCACTCAAAGATCGAATGTATTAGAATAATACATGTCAGTATTTTTCTGGTAGTTTTAGTAAGTCCTGTCTTCCACACATACTTTTTTTGTCTTAAATTCTGTATTAAGATTTATTTTGACTTAAAAACTGGGATACAGATTCTGCTTTATCTTTTTCC")

#De aantal G's en C's worden geteld            
aantal_g = sequentie.count('G')
aantal_c = sequentie.count('C')

#Het aantal G en C wordt bij elkaar opgeteld
aantal_gc = (aantal_g + aantal_c)

#De lengte van alles in de string
aantal_totaal = len(sequentie)

#het percentage van het aantal GC ten opzichte van het totale aantal
percentage = (aantal_gc / aantal_totaal * 100)

print("Het aantal GC's is: ", str(aantal_gc))
print("Het totale aantal nucleotiden is: ", str(aantal_totaal))
print("Het percentage van het aantal GC in de sequentie is: ", float(percentage),"%")




