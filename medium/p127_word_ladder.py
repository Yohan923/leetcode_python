"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation
sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
"""

from collections import deque

class Solution:
    def ladder_length(self, begin_word, end_word, word_list):

        def pre_processing(word_list, word_length):
            all_transforms = dict()
            for word in word_list:
                for i in range(word_length):
                    tmp = word[0:i] + "*" + word[i+1:]

                    if tmp not in all_transforms:
                        all_transforms[tmp] = [word]
                    else:
                        all_transforms[tmp].append(word)
            return all_transforms

        def bi_bfs(begin, end, transforms, word_length):

            begin_queue = deque([(begin, 1)])
            end_queue = deque([(end, 1)])

            begin_visited = {begin: 1}
            end_visited = {end: 1}

            while len(begin_queue) > 0 or len(end_queue) > 0:

                if len(begin_queue) > 0:
                    tmp1, level = begin_queue.popleft()
                    for i in range(word_length):
                        tmp = tmp1[0:i] + "*" + tmp1[i + 1:]
                        if tmp in transforms:
                            for word in transforms[tmp]:
                                if word in end_visited:
                                    return level + end_visited[word]
                                if word not in begin_visited:
                                    begin_visited[word] = level + 1
                                    begin_queue.append((word, level+1))

                if len(end_queue) > 0:
                    tmp2, level = end_queue.popleft()
                    for i in range(word_length):
                        tmp = tmp2[0:i] + "*" + tmp2[i + 1:]
                        if tmp in transforms:
                            for word in transforms[tmp]:
                                if word in begin_visited:
                                    return level + begin_visited[word]
                                if word not in end_visited:
                                    end_visited[word] = level + 1
                                    end_queue.append((word, level+1))

            return 0

        if end_word not in word_list:
            return 0

        all_transforms = pre_processing(word_list, len(begin_word))

        return bi_bfs(begin_word, end_word, all_transforms, len(begin_word))

if __name__ == '__main__':
    Solution().ladder_length("lost"
,"cost"
,["most","fist","lost","cost","fish"])




