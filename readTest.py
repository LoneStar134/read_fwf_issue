import pandas as pd
pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 500)


def conv_str(x):
    return str(x)

col_widths = [3, 2, 2, 2, 2, 11, 2, 2, 3, 3, 2, 3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
col_names = ['AGE', 'AGE_NEONATE', 'AMONTH', 'AWEEKEND', 'DIED', 'DISCWT', 'DISPUNIFORM', 'DQTR', 'DRG', 'DRG24', 'DRGVER', 'DRG_NoPOA', 'DX1', 'DX2', 'DX3', 'DX4', 'DX5', 'DX6', 'DX7', 'DX8', 'DX9', 'DX10', 'DX11', 'DX12', 'DX13', 'DX14', 'DX15', 'DX16', 'DX17', 'DX18', 'DX19', 'DX20', 'DX21', 'DX22', 'DX23', 'DX24', 'DX25']
col_conv = {'AGE': conv_str, 'AGE_NEONATE': conv_str, 'AMONTH': conv_str, 'AWEEKEND': conv_str, 'DIED': conv_str, 'DISCWT': conv_str, 'DISPUNIFORM': conv_str, 'DQTR': conv_str, 'DRG': conv_str, 'DRG24': conv_str, 'DRGVER': conv_str, 'DRG_NoPOA': conv_str, 'DX1': conv_str, 'DX2': conv_str, 'DX3': conv_str, 'DX4': conv_str, 'DX5': conv_str, 'DX6': conv_str, 'DX7': conv_str, 'DX8': conv_str, 'DX9': conv_str, 'DX10': conv_str, 'DX11': conv_str, 'DX12': conv_str, 'DX13': conv_str, 'DX14': conv_str, 'DX15': conv_str, 'DX16': conv_str, 'DX17': conv_str, 'DX18': conv_str, 'DX19': conv_str, 'DX20': conv_str, 'DX21': conv_str, 'DX22': conv_str, 'DX23': conv_str, 'DX24': conv_str, 'DX25': conv_str}

print 'THE FOLLOWING EXAMPLE FAILS TO PROPERLY COERCE THE COLUMNS WITH BLANK DATA VALUES STARTING AT COLUMN DX8'
df1 = pd.read_fwf('file:./sample_fwf-1.txt', widths=col_widths, names=col_names, converters=col_conv)

print df1
for k in df1.keys():
    print k + ' / ' + str(df1[k][0].__class__)

print 'THE FOLLOWING EXAMPLE FAILS TO PROPERLY COERCE THE COLUMNS WITH BLANK DATA VALUES STARTING AT COLUMN DX16'
df2 = pd.read_fwf('file:./sample_fwf-2.txt', widths=col_widths, names=col_names, converters=col_conv)

print df2
for k in df2.keys():
    print k + ' / ' + str(df2[k][0].__class__)
