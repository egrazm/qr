import tkinter as tk
from tkinter import filedialog, messagebox
import qrcode


class QRGenerator:
    """contiene la lógica de generación y guardado del código QR."""

    def generar(self, data: str, ruta: str) -> None:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(ruta)


class QRApp:
    """contiene la interfaz gráfica y el flujo de la aplicación."""

    def __init__(self):
        self.generator = QRGenerator()

        self.ventana = tk.Tk()
        self.ventana.title("Generador de QR")
        self.ventana.geometry("460x235")
        self.ventana.resizable(True, True)

        self._crear_widgets()

    def _crear_widgets(self):
        tk.Label(self.ventana, text="Texto o URL:").pack(pady=(15, 5))

        self.entrada_texto = tk.Entry(self.ventana, width=45)
        self.entrada_texto.pack(pady=(0, 10))
        self.entrada_texto.focus()

        tk.Label(self.ventana, text="Archivo de salida (.png):").pack(pady=(0, 5))

        self.entrada_archivo = tk.Entry(self.ventana, width=45)
        self.entrada_archivo.insert(0, "QR.png")
        self.entrada_archivo.pack(pady=(0, 8))

        tk.Button(
            self.ventana,
            text="Elegir ruta...",
            command=self.elegir_ruta
        ).pack(pady=(0, 8))

        tk.Button(
            self.ventana,
            text="Generar QR",
            command=self.generar_qr
        ).pack(pady=5)

        self.estado_var = tk.StringVar(value="Esperando datos...")
        tk.Label(self.ventana, textvariable=self.estado_var).pack(pady=(10, 0))

    #Captura y validación


    def _obtener_texto(self) -> str:
        texto = self.entrada_texto.get().strip()
        if not texto:
            raise ValueError("Ingresa un texto o URL para generar el QR.")
        return texto

    def _obtener_ruta(self) -> str:
        ruta = self.entrada_archivo.get().strip() or "QR.png"
        if not ruta.lower().endswith(".png"):
            ruta += ".png"
        return ruta


    #Eventos UI


    def elegir_ruta(self) -> None:
        ruta = filedialog.asksaveasfilename(
            title="Guardar QR como",
            defaultextension=".png",
            filetypes=[("Imagen PNG", "*.png"), ("Todos los archivos", "*.*")],
            initialfile="QR.png",
        )
        if ruta:
            self.entrada_archivo.delete(0, tk.END)
            self.entrada_archivo.insert(0, ruta)

    def generar_qr(self) -> None:
        try:
            texto = self._obtener_texto()
            ruta = self._obtener_ruta()

            self.generator.generar(texto, ruta)

            self.estado_var.set(f"QR generado: {ruta}")
            messagebox.showinfo("Listo", f"Se generó el archivo:\n{ruta}")

        except ValueError as error:
            messagebox.showwarning("Dato faltante", str(error))

        except OSError as error:
            messagebox.showerror(
                "Error al guardar",
                f"No se pudo guardar el archivo:\n{error}"
            )

    def run(self) -> None:
        self.ventana.mainloop()


#Punto de entrada

if __name__ == "__main__":
    app = QRApp()
    app.run()
