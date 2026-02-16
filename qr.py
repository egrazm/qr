import tkinter as tk
from tkinter import filedialog, messagebox

import qrcode


def generar_qr() -> None:
    data = entrada_texto.get().strip()

    if not data:
        messagebox.showwarning("Dato faltante", "Ingresa un texto o URL para generar el QR.")
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    ruta_salida = entrada_archivo.get().strip()
    if not ruta_salida:
        ruta_salida = "QR.png"
    if not ruta_salida.lower().endswith(".png"):
        ruta_salida += ".png"

    img = qr.make_image(fill_color="black", back_color="white")
    try:
        img.save(ruta_salida)
    except OSError as error:
        messagebox.showerror("Error al guardar", f"No se pudo guardar el archivo:\n{error}")
        return

    estado_var.set(f"QR generado: {ruta_salida}")
    messagebox.showinfo("Listo", f"Se genero el archivo:\n{ruta_salida}")


def elegir_ruta() -> None:
    ruta = filedialog.asksaveasfilename(
        title="Guardar QR como",
        defaultextension=".png",
        filetypes=[("Imagen PNG", "*.png"), ("Todos los archivos", "*.*")],
        initialfile="QR.png",
    )
    if ruta:
        entrada_archivo.delete(0, tk.END)
        entrada_archivo.insert(0, ruta)


ventana = tk.Tk()
ventana.title("Generador de QR")
ventana.geometry("460x235")
ventana.resizable(False, False)

tk.Label(ventana, text="Texto o URL:").pack(pady=(15, 5))

entrada_texto = tk.Entry(ventana, width=45)
entrada_texto.pack(pady=(0, 10))
entrada_texto.focus()

tk.Label(ventana, text="Archivo de salida (.png):").pack(pady=(0, 5))
entrada_archivo = tk.Entry(ventana, width=45)
entrada_archivo.insert(0, "QR.png")
entrada_archivo.pack(pady=(0, 8))

tk.Button(ventana, text="Elegir ruta...", command=elegir_ruta).pack(pady=(0, 8))
tk.Button(ventana, text="Generar QR", command=generar_qr).pack(pady=5)

estado_var = tk.StringVar(value="Esperando datos...")
tk.Label(ventana, textvariable=estado_var).pack(pady=(10, 0))

ventana.mainloop()
