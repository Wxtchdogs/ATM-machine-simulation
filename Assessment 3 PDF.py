from pypdf import PdfMerger, PdfWriter, PdfReader

#---------------Merge---------------#
pdfs = ['example.pdf', 'example2.pdf']

merge = PdfMerger()

for item in pdfs:
    merge.append(item)

merge.write("Merged.pdf")
merge.close()

print("File Merged. Output = Merged.pdf")
#---------------Merge---------------#

#---------------Rotate---------------#
reader = PdfReader("Merged.pdf")
writer = PdfWriter()

writer.add_page(reader.pages[0])
writer.pages[0].rotate(90)

with open("Rotated.pdf", "wb") as fp:
    writer.write(fp)

print("File rotated. Output = Rotated.pdf")
#---------------Rotate---------------#

#---------------Encrypt---------------#
writer.encrypt("secret key")

with open("Encrypted.pdf", "wb") as fp:
    writer.write(fp)

print("File encrypted. File = Encrypted.pdf")
#---------------Encrypt---------------#

#---------------Decrypt---------------#
writer = PdfWriter()
reader = PdfReader("Encrypted.pdf")

if reader.is_encrypted:
    reader.decrypt("secret key")

for page in reader.pages:
    writer.add_page(page)

with open("Decrypted.pdf", "wb") as f:
    writer.write(f)

print("File decrypted. File = decrypted.pdf")