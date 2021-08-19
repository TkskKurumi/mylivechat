import pic2pic
from PIL import Image
def addBorder(im,border_width,bg=(0,0,0,0)):
	w,h=im.size
	ret=Image.new(im.mode,(w+border_width*2,h+border_width*2),bg)
	ret.paste(im,box=(border_width,border_width))
	return ret
def richtext(contents,width,bg=(0,0,0,0),fill=(0,0,0,255),font_size=12,border_width=None, \
				x_align=0,y_align=1,line_space=None):
	if(border_width is None):
		border_width=width//7
	if(line_space is None):
		line_space=border_width
	_contents=list()
	for i in contents:
		if(isinstance(i,str)):
			_contents.extend(list(i))
		else:
			_contents.append(i)
	contents=_contents
	for idx,i in enumerate(contents):
		if(isinstance(i,str)):
			_i=pic2pic.txt2im(i,fixedHeight=font_size,fill=fill)
			contents[idx]=_i
		elif(isinstance(i,Image.Image)):
			_i=i
			if(i.size[0]>width-border_width*2):
				_i=pic2pic.fixWidth(_i,width-border_width*2)
			_i=addBorder(_i,border_width)
			contents[idx]=i
	row=list()
	_row=list()
	_row_width=0
	for idx,i in contents:
		_width,_height=i.size
		if(_row_width+_width>width):
			row.append(_row)
			_row_width=0
			_row=list()
		_row.append(i)
		_row_width+=_width
	row.append(_row)
	row_im=list()
	for _row in row:
		row_height=0
		row_width=0
		for content in _row:
			w,h=content.size
			row_height=max(row_height,h)
			row_width+=w
		
		