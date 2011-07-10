import os
import unittest
import re

class ConwayIO():
	def ConwayIO(self):
		self.rows = 0
		self.columns = 0
	
	def check_file_exists(self,filename):
		return os.path.isfile(filename)

	def process_file(self,filename):
		if(check_file_exists(filename)):
			lines = file_open(filename).readlines()
			if check_matrix_size(lines[0]):
			 	read_matrix_rows_cols(lines[0])
				if (check_matrix_integrity(lines[1:self.rows]) and check_content_integrity(lines[1:self.rows])):
					return False
 				
	def file_open(self,filename):
		return open(filename)
	
	def read_matrix_rows_cols(self,line):
		matrix_size =  line.split()
		self.rows = int(matrix_size[0])	
		self.columns = int(matrix_size[1])

	def check_matrix_size(self,line):
		matrix_size = line.split()
		if(len(matrix_size) == 2):
			if(matrix_size[0].isdigit() and matrix_size[1].isdigit()):
				return True 
		return False	 

	def check_matrix_integrity(self,lines):
		if(len(lines)==self.rows):
			for line in lines:
				if((len(line.strip()) != self.columns)):
					return False
			return True
		return False

	def check_content_integrity(self,lines):
	# ^((-*)+)
		invalid_pattern = re.compile('^((-*)+)')				
		for line in lines :
			match = invalid_pattern.match(line) 
			if(match != None):
				 return False
		return True
		
class TestConwayFunctions(unittest.TestCase):

	def setUp(self):
		self.filename = 'conwayinput.txt'
		self.conwayIO = ConwayIO()

	def test_input_file_exists(self):
        #  Check for the existance of the input file for the conway game
		self.assertTrue(self.conwayIO.check_file_exists(self.filename))

	def test_input_file_matrix_size(self):
		#check the first line of input file is a matrix size
		self.assertTrue(self.conwayIO.check_matrix_size(self.conwayIO.file_open(self.filename).readlines()[0]))

	def test_read_matrix_conf(self):
		input = open(self.filename)
		line = input.readline()
		matrix_size =  line.split()
		rows = int(matrix_size[0])
		columns = int(matrix_size[1])
		self.conwayIO.read_matrix_rows_cols(self.conwayIO.file_open(self.filename).readlines()[0])
		self.assertEqual(self.conwayIO.rows, rows)
		self.assertEqual(self.conwayIO.columns, columns)


	def test_input_rows_and_columns(self):
		input = open(self.filename)
		lines = input.readlines()
		lines = lines[1:len(lines)] 
		self.conwayIO.rows = len(lines)
		self.conwayIO.columns = len(lines[0].strip())

		self.assertTrue(self.conwayIO.check_matrix_integrity(lines), "Matrix integrity failed")

#    def test_choice(self):
#        element = random.choice(self.seq)
#        self.assertTrue(element in self.seq)
#
#    def test_sample(self):
#        self.assertRaises(ValueError, random.sample, self.seq, 20)
#        for element in random.sample(self.seq, 5):
#            self.assertTrue(element in self.seq)

if __name__ == '__main__':
    unittest.main()

	
