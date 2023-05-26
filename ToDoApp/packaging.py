#it is required to import manually import these packages when using pyinstaller
#note: for some reason, after packaging darkdetect need to be copied manually in to dist folder on macOS
import tkinter as tk
from tkinter import *
from customtkinter import *
from tkinter import filedialog
from tkinter import font
import distutils
from distutils import *
import darkdetect
from darkdetect import *
import ctypes.util
from tkinter import ttk