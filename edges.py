
def edgesFunct(graphJ, graphA):
    graphJ.add_edge('5010', '5011', 5)
    graphJ.add_edge('5011', '5012', 5)
    graphJ.add_edge('5012', '5013', 5)
    graphJ.add_edge('5013', '5014', 5)
    graphJ.add_edge('5014', '5015', 5)



    #fila 51
    graphJ.add_edge('5110', '5111', 10)
    graphJ.add_edge('5111', '5112', 10)
    graphJ.add_edge('5112', '5113', 10)
    graphJ.add_edge('5113', '5114', 10)
    graphJ.add_edge('5114', '5115', 10)


    #50-51
    graphJ.add_edge('5010', '5110', 5)
    graphJ.add_edge('5011', '5111', 5)
    graphJ.add_edge('5012', '5112', 7)
    graphJ.add_edge('5013', '5113', 7)
    graphJ.add_edge('5014', '5114', 7)
    graphJ.add_edge('5015', '5115', 5)



    #fila 52
    graphJ.add_edge('5210', '5211', 5)
    graphJ.add_edge('5211', '5212', 5)
    graphJ.add_edge('5212', '5213', 5)
    graphJ.add_edge('5213', '5214', 5)
    graphJ.add_edge('5214', '5215', 5)


    #51-52
    graphJ.add_edge('5110', '5210', 5)
    graphJ.add_edge('5111', '5211', 5)
    graphJ.add_edge('5112', '5212', 7)
    graphJ.add_edge('5113', '5213', 7)
    graphJ.add_edge('5114', '5214', 7)
    graphJ.add_edge('5115', '5215', 5)


    #fila 53
    graphJ.add_edge('5310', '5311', 5)
    graphJ.add_edge('5311', '5312', 5)
    graphJ.add_edge('5312', '5313', 5)
    graphJ.add_edge('5313', '5314', 5)
    graphJ.add_edge('5314', '5315', 5)


    #52-53
    graphJ.add_edge('5210', '5310', 5)
    graphJ.add_edge('5211', '5311', 5)
    graphJ.add_edge('5212', '5312', 7)
    graphJ.add_edge('5213', '5313', 7)
    graphJ.add_edge('5214', '5314', 7)
    graphJ.add_edge('5215', '5315', 5)


    #fila 54
    graphJ.add_edge('5410', '5411', 5)
    graphJ.add_edge('5411', '5412', 5)
    graphJ.add_edge('5412', '5413', 5)
    graphJ.add_edge('5413', '5414', 5)
    graphJ.add_edge('5414', '5415', 5)


    #53-54
    graphJ.add_edge('5310', '5410', 5)
    graphJ.add_edge('5311', '5411', 5)
    graphJ.add_edge('5312', '5412', 7)
    graphJ.add_edge('5313', '5413', 7)
    graphJ.add_edge('5314', '5414', 7)
    graphJ.add_edge('5315', '5415', 5)


    #fila 55
    graphJ.add_edge('5510', '5511', 5)
    graphJ.add_edge('5511', '5512', 5)
    graphJ.add_edge('5512', '5513', 5)
    graphJ.add_edge('5513', '5514', 5)
    graphJ.add_edge('5514', '5515', 5)

    
    #54-55
    graphJ.add_edge('5410', '5510', 5)
    graphJ.add_edge('5411', '5511', 5)
    graphJ.add_edge('5412', '5512', 7)
    graphJ.add_edge('5413', '5513', 7)
    graphJ.add_edge('5414', '5514', 7)
    graphJ.add_edge('5415', '5515', 5)


#aristas andreina

    #fila 50
    graphA.add_edge('5010', '5011', 7)
    graphA.add_edge('5011', '5012', 7)
    graphA.add_edge('5012', '5013', 7)
    graphA.add_edge('5013', '5014', 7)
    graphA.add_edge('5014', '5015', 7)



    #fila 51
    graphA.add_edge('5110', '5111', 12)
    graphA.add_edge('5111', '5112', 12)
    graphA.add_edge('5112', '5113', 12)
    graphA.add_edge('5113', '5114', 12)
    graphA.add_edge('5114', '5115', 12)


    #50-51
    graphA.add_edge('5010', '5110', 7)
    graphA.add_edge('5011', '5111', 7)
    graphA.add_edge('5012', '5112', 9)
    graphA.add_edge('5013', '5113', 9)
    graphA.add_edge('5014', '5114', 9)
    graphA.add_edge('5015', '5115', 7)



    #fila 52
    graphA.add_edge('5210', '5211', 7)
    graphA.add_edge('5211', '5212', 7)
    graphA.add_edge('5212', '5213', 7)
    graphA.add_edge('5213', '5214', 7)
    graphA.add_edge('5214', '5215', 7)

    #51-52
    graphA.add_edge('5110', '5210', 7)
    graphA.add_edge('5111', '5211', 7)
    graphA.add_edge('5112', '5212', 9)
    graphA.add_edge('5113', '5213', 9)
    graphA.add_edge('5114', '5214', 9)
    graphA.add_edge('5115', '5215', 7)


    #fila 53
    graphA.add_edge('5310', '5311', 7)
    graphA.add_edge('5311', '5312', 7)
    graphA.add_edge('5312', '5313', 7)
    graphA.add_edge('5313', '5314', 7)
    graphA.add_edge('5314', '5315', 7)


    #52-53
    graphA.add_edge('5210', '5310', 7)
    graphA.add_edge('5211', '5311', 7)
    graphA.add_edge('5212', '5312', 9)
    graphA.add_edge('5213', '5313', 9)
    graphA.add_edge('5214', '5314', 9)
    graphA.add_edge('5215', '5315', 7)


    #fila 54
    graphA.add_edge('5410', '5411', 7)
    graphA.add_edge('5411', '5412', 7)
    graphA.add_edge('5412', '5413', 7)
    graphA.add_edge('5413', '5414', 7)
    graphA.add_edge('5414', '5415', 7)


    #53-54
    graphA.add_edge('5310', '5410', 7)
    graphA.add_edge('5311', '5411', 7)
    graphA.add_edge('5312', '5412', 9)
    graphA.add_edge('5313', '5413', 9)
    graphA.add_edge('5314', '5414', 9)
    graphA.add_edge('5315', '5415', 7)


    #fila 55
    graphA.add_edge('5510', '5511', 7)
    graphA.add_edge('5511', '5512', 7)
    graphA.add_edge('5512', '5513', 7)
    graphA.add_edge('5513', '5514', 7)
    graphA.add_edge('5514', '5515', 7)


    #54-55
    graphA.add_edge('5410', '5510', 7)
    graphA.add_edge('5411', '5511', 7)
    graphA.add_edge('5412', '5512', 9)
    graphA.add_edge('5413', '5513', 9)
    graphA.add_edge('5414', '5514', 9)
    graphA.add_edge('5415', '5515', 7)