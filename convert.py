import os
import sys
from PySide6.QtWidgets import QApplication, QFileDialog, QInputDialog, QMessageBox, QVBoxLayout, QDialog, QDialogButtonBox, QComboBox
import openers.nhf_bg as bg

def select_nhf_file():
    file_dialog = QFileDialog()
    nhf_file, _ = file_dialog.getOpenFileName(
        None, "Select .nhf source file", "", "NHF files (*.nhf)"
    )
    return nhf_file

class GeometryDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tip Geometry")
        self.layout = QVBoxLayout()

        self.combo = QComboBox()
        self.combo.addItems(["sphere", "cone", "pyramid"])
        self.layout.addWidget(self.combo)

        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        self.layout.addWidget(self.button_box)

        self.setLayout(self.layout)

    def get_geometry(self):
        if self.exec() == QDialog.Accepted:
            return self.combo.currentText()
        return None

def get_tip_geometry():    
    dialog = GeometryDialog()
    #geometry = dialog.get_geometry()
    #if not geometry:
    #    return None, None
    geometry = "sphere"

    if geometry == "sphere":
        radius, ok = QInputDialog.getDouble(
            None, "Sphere Radius", "Enter the radius in um (0 to 1000):", 0.07, 0, 1000, 3
        )
        if not ok:
            return None, None
        return geometry, radius
    elif geometry in ["cone", "pyramid"]:
        angle, ok = QInputDialog.getDouble(
            None, "Tip Angle", "Enter the angle in degrees:", 0, 0, 180, 1
        )
        if not ok:
            return None, None
        return geometry, angle
    else:
        QMessageBox.critical(None, "Error", "Invalid geometry type entered.")
        return None, None

def select_hdf5_file(default_folder, default_filename):
    file_dialog = QFileDialog()
    hdf5_file, _ = file_dialog.getSaveFileName(
        None, "Select output .hdf5 file", os.path.join(default_folder, default_filename), "HDF5 files (*.hdf5)"
    )
    return hdf5_file

def main():    
    nhf_file = select_nhf_file()
    if not nhf_file:
        print("No .nhf file selected.")
        return
    
    curves,coordinates,k = bg.open(nhf_file)

    geometry, radius = get_tip_geometry()
    if not geometry:
        print("Invalid geometry or value.")
        return

    default_folder = os.path.dirname(nhf_file)
    default_filename = os.path.splitext(os.path.basename(nhf_file))[0] + ".hdf5"
    hdf5_file = select_hdf5_file(default_folder, default_filename)
    if not hdf5_file:
        print("No .hdf5 file selected.")
        return

    bg.save( hdf5_file,curves,coordinates,k,radius)

    print(f"NHF File: {nhf_file}")
    print(f"Radius: {radius} Elastic constant: {k}")
    print(f"HDF5 File: {hdf5_file}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main()