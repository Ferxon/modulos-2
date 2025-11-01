import numpy as np
import pandas as pd
import sqlite3

miConexion = sqlite3.connect("GestionProductos")
miCursor=miConexion.cursor()

# miCursor.execute("DELETE FROM PRODUCTOS WHERE NOMBRE_ARTICULO='pantalon'")



miConexion.commit()

miConexion.close()