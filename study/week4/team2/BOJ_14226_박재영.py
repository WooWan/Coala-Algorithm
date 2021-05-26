{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "18\n",
      "8\n"
     ]
    }
   ],
   "source": [
    "from collections import deque\n",
    "\n",
    "s = int(input())\n",
    "board = [[-1]* (s+1) for _ in range(s+1)]\n",
    "\n",
    "de = deque()\n",
    "de.append((1,0))\n",
    "board[1][0] = 0\n",
    "    \n",
    "while de:\n",
    "    x, y = de.popleft()\n",
    "        \n",
    "    #1번\n",
    "    if board[x][x] == -1:\n",
    "        board[x][x] = board[x][y] + 1\n",
    "        de.append((x,x))\n",
    "    #2번\n",
    "    if x+y <= s and board[x+y][y] == -1:\n",
    "        board[x+y][y] = board[x][y] + 1\n",
    "        de.append((x+y, y))\n",
    "    #3번\n",
    "    if x-1 >= 0 and board[x-1][y] == -1:\n",
    "        board[x-1][y] = board[x][y] + 1\n",
    "        de.append((x-1, y))\n",
    "         \n",
    "time = -1\n",
    "\n",
    "for i in range(s+1):\n",
    "    if board[s][i] != -1:\n",
    "        if time == -1 or time > board[s][i]:\n",
    "            time = board[s][i]\n",
    "\n",
    "\n",
    "print(time)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
