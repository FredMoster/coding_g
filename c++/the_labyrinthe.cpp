// PATH FINDING
// BREADTH FIRST SEARCH

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

typedef vector<string> Maze;

string goBack(string& path, int& steps) {
    string result;
    switch ( path[--steps] ) {
        case 'U': result = "DOWN"; break;
        case 'D': result = "UP"; break;
        case 'R': result = "LEFT"; break;
        case 'L': result = "RIGHT"; break;
    }
    path.pop_back();
    return result;
}

string recalculatePathBack(vector<vector<int> >& distance,
        const int KR,
        const int KC) {

    string result = "";
    int vB = distance[KR][KC];
    const int vU = distance[KR-1][KC];
    const int vD = distance[KR+1][KC];
    const int vL = distance[KR][KC-1];
    const int vR = distance[KR][KC+1];

    if (vU != 0 && vU < vB) result = "UP";
    if (vD != 0 && vD < vB) result = "DOWN";
    if (vL != 0 && vL < vB) result = "LEFT";
    if (vR != 0 && vR < vB) result = "RIGHT";

    return result;
}

void computeDistance (vector<vector<int> >& distance,
        const int KR,
        const int KC,
        const Maze& maze,
        const bool light=false) {

    vector<int> v;
    int& vB = distance[KR][KC];
    const int& vU = distance[KR-1][KC];
    const int& vD = distance[KR+1][KC];
    const int& vL = distance[KR][KC-1];
    const int& vR = distance[KR][KC+1];

    if (vB != 0) v.push_back(vB);
    if (vU != 0) v.push_back(vU+1);
    if (vD != 0) v.push_back(vD+1);
    if (vL != 0) v.push_back(vL+1);
    if (vR != 0) v.push_back(vR+1);
    if (v.size() == 0 ) {
        if (maze[KR][KC] == 'C' || maze[KR][KC] == 'T') distance[KR][KC] = 1;
    } else {
        vector<int>::iterator result = min_element(v.begin(), v.end());
        vB = result[0];
    }

    // adjust
    if ( vU > vB+1 ) computeDistance(distance, KR-1, KC, maze, light);
    if ( vD > vB+1 ) computeDistance(distance, KR+1, KC, maze, light);
    if ( vL > vB+1 ) computeDistance(distance, KR, KC-1, maze, light);
    if ( vR > vB+1 ) computeDistance(distance, KR, KC+1, maze, light);
    if (!light) {
      if (vU == 0 && (maze[KR-1][KC] == '.' || maze[KR-1][KC] == 'C')) computeDistance(distance, KR-1, KC, maze);
      if (vD == 0 && (maze[KR+1][KC] == '.' || maze[KR+1][KC] == 'C')) computeDistance(distance, KR+1, KC, maze);
      if (vL == 0 && (maze[KR][KC-1] == '.' || maze[KR][KC-1] == 'C')) computeDistance(distance, KR, KC-1, maze);
      if (vR == 0 && (maze[KR][KC+1] == '.' || maze[KR][KC+1] == 'C')) computeDistance(distance, KR, KC+1, maze);
    }
}

int main()
{
    int R; // number of rows.
    int C; // number of columns.
    int A; // number of rounds between the time the alarm countdown is activated and the time the alarm goes off.
    cin >> R >> C >> A; cin.ignore();

    string path;
    int steps = 0;
    bool reached = false;
    bool found = false;
    int GR = -1;
    int GC = -1;
    vector<int> emptyDist(C, 0);
    vector<vector<int> > dist_T(R, emptyDist);
    vector<vector<int> > dist_G(R, emptyDist);
    vector<bool> emptyLine(C, false);
    vector<vector<bool> > visited(R, emptyLine);

    // game loop
    while (1) {
        int KR; // row where Kirk is located.
        int KC; // column where Kirk is located.
        string result = "";
        cin >> KR >> KC; cin.ignore();
        visited[KR][KC] = true;
        Maze maze;
        for (int i = 0; i < R; i++) {
            string ROW; // C of the characters in '#.TC?' (i.e. one line of the ASCII maze).
            cin >> ROW; cin.ignore();
            maze.push_back(ROW);
            if (!found) {
                for (int j = 0; j < C; j++) {
                    if (maze[i][j] == 'C') {
                        GR = i;
                        GC = j;
                        found = true;
                        computeDistance(dist_G, GR, GC, maze, true);
                    }
                }
            }
        }

        if (reached) {
            if (steps > A) {
                if (dist_T[KR][KC] > A) computeDistance(dist_T, KR, KC, maze);
                result = recalculatePathBack(dist_T, KR, KC);
            } else { // easy path, simply go back
                result = goBack(path, steps);
            }
        } else {
            computeDistance(dist_T,KR,KC,maze);
            if (found) {
                computeDistance(dist_G, KR, KC, maze, true);
                if (dist_T[GR][GC] <= A+1) {
                    // 1 step away
                    if (KC == GC) {
                        if (KR+1 == GR) {
                            result = "DOWN";
                            reached = true;
                        } else if (KR-1 == GR) {
                            result = "UP";
                            reached = true;
                        }
                    } else if (KR == GR) {
                        if (KC+1 == GC) {
                            result = "RIGHT";
                            reached = true;
                        } else if (KC-1 == GC) {
                            result = "LEFT";
                            reached = true;
                        }
                    }
                    if ( result == "" ) result = recalculatePathBack(dist_G, KR, KC);
                }
            }
            if (!reached && result == "") {
                if ( maze[KR][KC+1] == '.' && !visited[KR][KC+1]) result = "RIGHT";
                else if ( maze[KR+1][KC] == '.' && !visited[KR+1][KC]) result = "DOWN";
                else if ( maze[KR-1][KC] == '.' && !visited[KR-1][KC]) result = "UP";
                else if ( maze[KR][KC-1] == '.' && !visited[KR][KC-1]) result = "LEFT";
                else result = "";
            }
            if (result != "") {
                path += result[0];
                steps++;
            } else {
                result = goBack(path, steps);
            }
        }
        cout << result << endl; // Kirk's next move (UP DOWN LEFT or RIGHT).
    }
}
