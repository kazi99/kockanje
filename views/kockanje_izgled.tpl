<!DOCTYPE html>
<html> 
    <head>
        <title>Kockanje</title>
    </head>
    <table>
        <tr>
            <th>Kombinacije</th>
            <th>Točke</th>
        </tr>
        % for i, key in enumerate(tabela):
        <tr>
            % if key in odprte_kombinacije and met != ZACETEK:
            <td>
                <form action='/izberi-kombinacjo/{{ i }}/' method="POST">
                    <input type="hidden" name="{{ key }}"> 
                    <input type="submit" value="{{ key }}">
                </form>
            </td>
            <td>{{ tabela[key] }}</td>
            % else:
            <td>{{ key }}</td>
            <td>{{ tabela[key] }}</td>
            % end
        </tr>
        % end
    </table>

    %if konec:
    <table>
        <tr>
            % for ime_kocke in 'ABCDE':
            <th>{{ ime_kocke }}</th>
            %end
        </tr>
        <tr>
            % for kocka in met:
            <td>{{ kocka }}</td>
            %end
        </tr>
    </table>
    % elif st_metov == STEVILO_METOV:
    <table>
        <tr>
            % for ime_kocke in 'ABCDE':
            <th>{{ ime_kocke }}</th>
            %end
        </tr>
        <tr>
            % for kocka in met:
            <td>{{ kocka }}</td>
            %end
        </tr>
    </table>
        <form action='/izberi-met/' method="POST">
            <input type="submit" value="Vrži">
        </form>
    % elif st_metov > 0:
    <table>
        <form action='/izberi-met/' method="POST">
            <tr>
                <td><input type="checkbox" name="a"> A </td>
                <td><input type="checkbox" name="b"> B </td>
                <td><input type="checkbox" name="c"> C </td>
                <td><input type="checkbox" name="d"> D </td>
                <td><input type="checkbox" name="e"> E </td>
                <input type="submit" value="Vrži še enkrat">
            </tr>
            <tr>
                % for kocka in met:
                <td>{{ kocka }}</td>
                %end
            </tr>
            <tr>
                {{ met }}   {{ st_metov }}
            </tr>
        </form>
    </table>
    % else:
    <table>
        <tr>
                % for ime_kocke in 'ABCDE':
                <th>{{ ime_kocke }}</th>
                %end
            </tr>
            <tr>
                % for kocka in met:
                <td>{{ kocka }}</td>
                %end
        </tr>
    </table>
    % end

    <form action='/reset/' action="GET">
        <input type="submit" value="Resetiraj" name="resetiranje">
    </form>
</html>