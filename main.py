from desktop import Desktop
from notebook import Notebook 


desktop = Desktop()
notebook = Notebook()

desktop.cadastrar("Gigabyte", "Preto", "650W")

print(f'Informações Desktop')
desktop.getInformacoes()

print(f'Informações Notebook')
notebook.cadastrar("Asus", "Branco", "35hs")
notebook.getInformacoes()