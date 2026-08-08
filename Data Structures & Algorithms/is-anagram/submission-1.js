class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) return false

        const counts = new Array(26).fill(0);
        const ordinal = 'a'.charCodeAt(0)

        for (let i = 0; i < s.length; i += 1) {
            counts[s[i].charCodeAt(0) - ordinal] +=  1;
            counts[t[i].charCodeAt(0) - ordinal] -= 1;
        }

        for (const count of counts) {
            if (count !== 0) return false;
        }

        return true
    }
}
