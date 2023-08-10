import sys

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.uic import loadUi


class ForSaleList(QWidget):
    def __init__(self, info_, parent=None):
        super().__init__(parent)
        loadUi('./ui_file/CU_list_item.ui', self)
        store_type = info_.rea_store_ctg
        contract_area = info_.rea_contract_area
        dedicaed_area = info_.rea_dedicaed_area
        realty_type = info_.rea_realty_ctg
        rental_price = info_.reg_rantal_price
        deposit = info_.reg_deposit
        selling_price = info_.reg_selling_price
        if rental_price is None:
            rental_price = "-"
        if deposit is None:
            deposit = '-'
        if selling_price is None:
            selling_price = '-'
        self.label.setText(f' {store_type}  |  {realty_type}  |  {rental_price}  |  {deposit}  |  {selling_price}  |  '
                           f'{contract_area}m² | {dedicaed_area}m²')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = ForSaleList()
    myWindow.show()
    app.exec_()