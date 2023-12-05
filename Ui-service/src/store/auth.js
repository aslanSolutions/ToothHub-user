
// Intial state

const state = {
    email: '',
    userType: '',
    accessToken: ''
};

// Getters

const getters = {
    getEmail: (state) => state.email,
    getUserType: (state) => state.userType,
    getAccessToken: (state) => state.accessToken
};

// Mutations

const mutations = {
    setEmail: (state, email) => (state.email = email),
    setUserType: (state, userType) => (state.userType = userType),
    setAccessToken: (state, accessToken) => (state.accessToken = accessToken)
};

// Actions

const actions = {
    updateEmail: ({commit}, email) => {
        commit ('setEmail', email);
    },
    updateUserType: ({commit}, userType) => {
        commit ('setUserType', userType);
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