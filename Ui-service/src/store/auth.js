
// Intial state

const state = {
    email: '',
    type: '',
    accessToken: '',
    isLoggedIn: false
};

// Getters

const getters = {
    getEmail: (state) => state.email,
    getType: (state) => state.type,
    getAccessToken: (state) => state.accessToken,
    getIsLoggedIn: (state) => state.isLoggedIn
};

// Mutations

const mutations = {
    setEmail: (state, email) => (state.email = email),
    setType: (state, type) => (state.type = type),
    setAccessToken: (state, accessToken) => (state.accessToken = accessToken),
    setIsLoggedIn: (state, isLoggedIn) => (state.isLoggedIn = isLoggedIn)
};

// Actions

const actions = {
    updateEmail: ({commit}, email) => {
        commit ('setEmail', email);
    },
    updateType: ({commit}, type) => {
        commit ('setType', type);
    },
    updateAccessToken: ({commit}, accessToken) => {
        commit ('setAccessToken', accessToken)
    },
    updateIsLoggedIn: ({commit}, isLoggedIn) => {
        commit ('setIsLoggedIn', isLoggedIn)
    },
    resetVuexState: ({ commit }) => {
        commit('setEmail', '');
        commit('setType', '');
        commit('setAccessToken', '');
        commit('setIsLoggedIn', false);
      },
}

export default {
    state,
    getters,
    mutations,
    actions
}