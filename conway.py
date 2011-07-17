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
			 	read_matrix_size(lines[0])
				if (check_matrix_integrity(lines[1:self.rows]) and check_content_integrity(lines[1:self.rows])):
					return False
 				
	def file_open(self,filename):
		return open(filename)
	
	def read_matrix_size(self,line):
		matrix_size =  line.split()
		self.rows = int(matrix_size[0])	
		self.columns = int(matrix_size[1])

	def check_matrix_size(self,line):
		matrix_size = line.split()
		if(len(matrix_size) == 2):
			if(matrix_size[0].isdigit() and matrix_size[1].isdigit()):
				if(matrix_size[0] >= 3 and matrix_size[1] >= 3):
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
		invalid_pattern = re.compile('^[[-]*[\*]*]+')				
		
		for line in lines :
			match = invalid_pattern.match(line) 
			if(match != None):
				return False
		return True
	
	def check_valid_cell(self,i,j):
		if i < 0 or i > self.rows - 1:
			return False
		if j < 0 or j > self.columns - 1:
 			return False
		return True

	def get_valid_neighbours(self,i,j):
		valid_neighbours = []
		if (self.check_valid_cell(i - 1, j - 1)):
			valid_neighbours.append([i - 1, j - 1])

		if (self.check_valid_cell(i - 1, j)):
			valid_neighbours.append([i - 1, j])

		if (self.check_valid_cell(i - 1, j + 1)):
			valid_neighbours.append([i - 1, j + 1])

		if (self.check_valid_cell(i, j - 1)):
			valid_neighbours.append([i, j - 1])

		if (self.check_valid_cell(i, j + 1)):
			valid_neighbours.append([i, j + 1])

		if (self.check_valid_cell(i + 1, j - 1)):
			valid_neighbours.append([i + 1, j - 1])

		if (self.check_valid_cell(i + 1, j)):
			valid_neighbours.append([i + 1, j])

		if (self.check_valid_cell(i + 1, j + 1)):
			valid_neighbours.append([i + 1, j + 1])

		return valid_neighbours

class TestConwayFunctions(unittest.TestCase):
		
	def setUp(self):
		self.filename = 'conwayinput.txt'
		self.conwayIO = ConwayIO()
		files = open(self.filename)
		lines = files.readlines()
		self.rows = len(lines) - 1
		self.cols = len(lines[1].strip())
		self.valid_edge_cases = [[0,0],[0,self.cols - 1],[0,self.cols - 1],[1,0],[1,self.cols - 1],[self.rows - 1,0],[self.rows - 1,1],[self.rows - 1,self.cols - 1], [self.rows - 2,self.cols - 2]] 
		self.invalid_edge_cases = [[-1,0],[0,self.cols + 1],[-1,self.cols - 1],[self.rows,0],[self.rows,1],[self.rows,self.cols], [self.rows - 1,self.cols], [self.rows + 1, self.cols + 1]] 
		files.close()
	
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
		self.conwayIO.read_matrix_size(self.conwayIO.file_open(self.filename).readlines()[0])
		self.assertEqual(self.conwayIO.rows, rows)
		self.assertEqual(self.conwayIO.columns, columns)


	def test_input_rows_and_columns(self):
		input = open(self.filename)
		lines = input.readlines()
		lines = lines[1:len(lines)] 
		self.conwayIO.rows = len(lines)
		self.conwayIO.columns = len(lines[0].strip())
		self.assertTrue(self.conwayIO.check_matrix_integrity(lines), "Matrix integrity failed")

	def test_input_rows_and_columns(self):
		input = open(self.filename)
		lines = input.readlines()
		lines = lines[1:len(lines)] 
	
		self.assertTrue(self.conwayIO.check_content_integrity(lines), "Content integrity failed")

	def test_valid_cell(self):
		#Test the function to check if cells for a cell exist
		self.conwayIO.read_matrix_size(self.conwayIO.file_open(self.filename).readlines()[0])		
		[self.assertTrue(self.conwayIO.check_valid_cell(i,j), str(i)+","+str(j)+" is valid but did not pass through") for i,j in self.valid_edge_cases]		
		#print [(i, j) for i,j in self.valid_edge_cases]		
	def test_invalid_cell(self):
		#Test the function to check if cells for a cell exist
		self.conwayIO.read_matrix_size(self.conwayIO.file_open(self.filename).readlines()[0])		

		[self.assertFalse(self.conwayIO.check_valid_cell(i,j), str(i)+","+str(j)+" is invalid but passed through") for i,j in self.invalid_edge_cases]		

	def test_get_valid_neighbour(self):
		#Test the function to check if the correct number of neighbours are retrieved
		self.conwayIO.read_matrix_size(self.conwayIO.file_open(self.filename).readlines()[0])
		self.assertEquals(len(self.conwayIO.get_valid_neighbours(0,0)),3)	
		self.assertEquals(len(self.conwayIO.get_valid_neighbours(0,1)),5)	
		self.assertEquals(len(self.conwayIO.get_valid_neighbours(1,1)),8)	

if __name__ == '__main__':
    unittest.main()

	
