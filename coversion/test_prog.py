import currency_in_chars
import conversion_hindi


def test_conversion():
    assert currency_in_chars.conversion(982598256.67) == " ninty eight Crore twenty five Lakh ninty eight Thousand two Hundred and fifty six 67/10"
    
def test_conv_hindi():
    assert conversion_hindi.conv_hindi(452111511.67) == "  पैंतालीस करोड़ इकीस लाख ग्यारह हज़ार पांचसौ ग्यारह 67/100"









# import currency_in_chars
# # import pdb


# # pdb.set_trace()
# def test_conversion(input_value):
#     assert currency_in_chars.conversion(input_value) == " ninty seven Crore fifty six Lakh fourty eight Thousand two Hundred and fifty four 67/100"
#     # assert conversions.conversion(65452632.11) == "  six Crore fifty four Lakh fifty two Thousand six Hundred and thirty two 11/100"