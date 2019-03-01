# coding:gbk
# ����һ���࣬ʹ�������洢���ֺͶ�Ӧ��Ƶ��
class element:
	def __init__(self, x, y):
		self.character = x
		self.count = y

# ����洢���ּ���ӦƵ�ε��ֵ������ĺ���
def add_character(character,dic):
	# �������ĺ����ڴʵ�����δ���֣���֮��ӽ�ȥ������ֵΪ1
	if character not in dic:
		dic[character] = 1
	# �������ĺ��ִʵ����Ѿ��Ѿ���������֮��Ӧ��ֵ+1����
	else:
		dic[character] = dic[character] + 1

# �����б�Ժ��ְ�Ƶ�ν�������
def show(dic):
	# ����һ���б�
	result = []
	for key in dic:
		# ���ʵ��еĺ��ֺͶ�Ӧ��Ƶ�δ�����element����ʽ����ele
		ele = element(key,dic[key])
		# �����к��ֺͶ�ӦƵ�ε�ele���뵽result�б���
		result.append(ele)
	# ʹ��sort���б��������
	result.sort(key=lambda element:element.count,reverse = True)
	# �������ĺ��ּ���ӦƵ�ΰ�˳�����
	for ele in result:
		# ����ele.count��int���ͣ�������ele.character��ӣ�����ǿ��ת����string�ټӺ����
		print(ele.character + ' : ' + str(ele.count))

def get_paragraph(dic):
	while True:
		try:
			# �˴��û���EOF�ķ�ʽ��������
			line = input()
		except:
			# ���û��������룬����׽��EOF�쳣ʱ����
			break
		# ���������������ô����õ����뽻������add_character����
		else:
			for character in line:
				# �˴��ж��Ƿ�Ϊ����
				if character >= u'\u4e00' and character <= u'\u9fa5':

					add_character(character,dic)

dic = {}
get_paragraph(dic)
show(dic)