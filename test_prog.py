import currency_in_chars
import conversion_hindi
import conversion_marathi


def test_conversion():
    assert currency_in_chars.conversion(982598256.67) == " ninty eight Crore twenty five Lakh ninty eight Thousand two Hundred and fifty six 67/100"
    assert conversion_hindi.conv_hindi(452111511.67) == "  पैंतालीस करोड़ इकीस लाख ग्यारह हज़ार पांचसौ ग्यारह 67/100"
    assert conversion_marathi.conv_marathi(584526211.67) == "  अठ्ठावन्न करोड़ पंचेचाळीस लाख सव्वीस हज़ार दोनशे अकरा 67/100"
# def test_conv_hindi():
#     assert conversion_hindi.conv_hindi(452111511.67) == "  पैंतालीस करोड़ इकीस लाख ग्यारह हज़ार पांचसौ ग्यारह 67/100"
