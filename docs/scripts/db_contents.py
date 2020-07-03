r"""Scripts used to build documentation."""

import sdoc


def gen_rst_table():
    r"""Generate table of database contents in .rst format."""
    sdb = sdoc.SDOC(mode ='r')
    sdb.contents['id'] = sdb.contents.index
    sdb.contents = sdb.contents[['id', 'material ID', 'material', 'subgroup',
                                 'group',  'reference', 'state', 'phase',
                                 'temperature', 'path']]
    data = list(sdb.contents.values)
    data.insert(0, ['id', 'material ID', 'material', 'subgroup',
                    'group', 'reference', 'state', 'phase',
                    'temperature', 'path'])
    numcolumns = len(data[0])
    colsizes = [max(len(r[i]) for r in data) for i in range(numcolumns)]
    formatter = ' '.join('{:<%d}' % c for c in colsizes)
    rowsformatted = [formatter.format(*row) for row in data]
    line = formatter.format(*['=' * c for c in colsizes])
    output = line + '\n' + rowsformatted[0] + '\n' + line + '\n' \
                  + '\n'.join(rowsformatted[1:]) + '\n' + line
    return output


if __name__ == '__main__':
    print(gen_rst_table())
