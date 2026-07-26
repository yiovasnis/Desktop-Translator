import cv2

print("Versión:", cv2.__version__)
print("Archivo:", cv2.__file__)
print("Tiene cvtColor:", hasattr(cv2, "cvtColor"))