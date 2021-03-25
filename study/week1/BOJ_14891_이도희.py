{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10010011\n",
      "01010011\n",
      "11100011\n",
      "01010101\n",
      "8\n",
      "1 1\n",
      "2 1\n",
      "3 1\n",
      "4 1\n",
      "1 -1\n",
      "2 -1\n",
      "3 -1\n",
      "4 -1\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "from collections import deque\n",
    "         \n",
    "gear = []\n",
    "# 톱니바퀴 만들기\n",
    "for i in range(4):\n",
    "    gear.append(deque(list(input())))\n",
    "\n",
    "trial = int(input())\n",
    "for i in range(trial):\n",
    "    gearnum, direction = map(int,input().split(\" \"))\n",
    "    num = gearnum-1\n",
    "    right = gear[num][2] # 새 시도마다 초기화해주기\n",
    "    left = gear [num][6]\n",
    "    gear[num].rotate(direction)\n",
    "    origindirection = direction\n",
    "    \n",
    "    \n",
    "#Right\n",
    "    direction = origindirection\n",
    "    for i in range(num,3,1):\n",
    "        if right != gear[i+1][6]: # 오른쪽 톱니와 비교해서 다른 극이면 돌림\n",
    "            right = gear[i+1][2]\n",
    "            direction = -direction\n",
    "            gear[i+1].rotate(direction)\n",
    "        else:\n",
    "            break\n",
    "           \n",
    "#Left\n",
    "    direction = origindirection\n",
    "    for i in range(num,0,-1):\n",
    "        if left != gear[i-1][2]: # 왼쪽 톱니와 비교해서 다른 극이면 돌림\n",
    "            left = gear[i-1][6]\n",
    "            direction = -direction\n",
    "            gear[i-1].rotate(direction) \n",
    "        else:\n",
    "            break\n",
    "    \n",
    "\n",
    "result = 0\n",
    "for i in range(4):\n",
    "    if gear[i][0] == '1':\n",
    "        result += 2**i\n",
    "print(result)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
