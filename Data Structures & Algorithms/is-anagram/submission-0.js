class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) return false

        const sCounts = {};
        const tCounts = {};

        for (let i = 0; i < s.length; i += 1) {
            sCounts[s[i]] = sCounts[s[i]] ? sCounts[s[i]] + 1 : 1;
            tCounts[t[i]] = tCounts[t[i]] ? tCounts[t[i]] + 1 : 1;
        }

        for (const key of Object.keys(sCounts)) {
            if (sCounts[key] !== tCounts[key]) return false
        }

        return true
    }
}
