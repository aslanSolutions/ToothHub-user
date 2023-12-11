
// Intial state

const state = {
    email: '',
    type: '',
    accessToken: ''
};

// Getters

const getters = {
    getEmail: (state) => state.email,
    getType: (state) => state.type,
    getAccessToken: (state) => state.accessToken
};

// Mutations

const mutations = {
    setEmail: (state, email) => (state.email = email),
    setType: (state, type) => (state.type = type),
    setAccessToken: (state, accessToken) => (state.accessToken = accessToken)
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
    }
}

export default {
    state,
    getters,
    mutations,
    actions
}