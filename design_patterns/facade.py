import popen2

class PopenFacade:
    def execute(self, cmd):
        fout, fin, ferr = popen2.popen3(cmd)
        
        print cmd
        
        print '=' * 80
        print ' OUTPUT'
        print '=' * 80
        print fout.read()
        
        print '=' * 80
        print ' ERRORS'
        print '=' * 80
        print ferr.read()

pop = PopenFacade()

cmd = r'java -cp C:\jars\xslt_intercall xalanjava ./55.xml	./text_template.xsl ./out55.txt'
pop.execute(cmd)