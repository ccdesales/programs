class Image:
    pass
    
class GIFImage:
    pass
class JPEGImage:
    pass
    
class ImageProcessor:
    def getProcessor(self, image):
        if isinstance(image, GIFImage):
            return GIFProcessor()
        elif isinstance(image, JPEGImage):
            return JPEGProcessor()
    
class GIFProcessor(ImageProcessor):
    def process(self):
        print 'Processing GIF'
    
class JPEGProcessor(ImageProcessor):
    def process(self):
        print 'Processing JPEG'
    
    
gg = GIFImage()
jj = JPEGImage()

proc = ImageProcessor().getProcessor(gg)
proc.process()

proc = ImageProcessor().getProcessor(jj)
proc.process()

#>python -u "factory.py"
#Processing GIF
#Processing JPEG
#>Exit code: 0