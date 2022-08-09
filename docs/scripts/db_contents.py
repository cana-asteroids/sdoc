r"""Scripts used to build documentation."""

import sdoc


def gen_rst_table():
    r"""Generate table of database contents in .rst format."""
    sdb = sdoc.SDOC(mode ='r')
    sdb.contents['id'] = sdb.contents.index

    sdb.contents['wmin'] = sdb.contents['wmin'].astype("string")
    sdb.contents['wmax'] = sdb.contents['wmax'].astype("string")
    sdb.contents['res'] = sdb.contents['res'].astype("string")

    sdb.contents = sdb.contents[['id', 'mid', 'material', 'formula', 'group',
                      'phase', 'temp', 
                      'wmin', 'wmax', 'res', 
                      'hpath', 'ref']]

    data = sdb.contents.values.tolist()
    data.insert(0, ['id', 'mid', 'material', 'formula', 'group',
                      'phase', 'temp', 
                      'wmin', 'wmax', 'res', 
                      'hpath', 'ref'])
    # print(data[0])
    numcolumns = len(data[0])
    # print(len(data[0]))
    colsizes = []
    for i in range(numcolumns):
        # print(i)
        # print([r[i] for r in data])
    #     for r in data:
    #         print(r)
        colsizes.append(max([len(r[i]) for r in data]))
        # print(max([len(r[i]) for r in data]))
    # colsizes = [len(r[i]) for r in data for i in range(numcolumns)]
    # print(numcolumns, [len(r[numcolumns-1]) for r in data])
    formatter = ' '.join('{:<%d}' % c for c in colsizes)
    rowsformatted = [formatter.format(*row) for row in data]
    line = formatter.format(*['=' * c for c in colsizes])
    output = line + '\n' + rowsformatted[0] + '\n' + line + '\n' \
                  + '\n'.join(rowsformatted[1:]) + '\n' + line
    return output


if __name__ == '__main__':
    print(gen_rst_table())
